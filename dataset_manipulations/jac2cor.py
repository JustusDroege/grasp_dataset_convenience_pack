from PIL import Image
import os
import math
import cv2
import argparse
import numpy as np

SCALE_FACTOR = 640.0/1024

def visualize_grasps(img_original, grasps, window_name):
    img = img_original.copy()
    for grasp in grasps:
        coord0 = grasp[0]
        coord1 = grasp[1]
        coord2 = grasp[2]
        coord3 = grasp[3]
        # attention BGR in OpenCV
        cv2.line(img, (int(coord0[0]), int(coord0[1])), (int(coord1[0]), int(coord1[1])), (10, 200, 10), 1)
        cv2.line(img, (int(coord1[0]), int(coord1[1])), (int(coord2[0]), int(coord2[1])), (200, 15, 0), 1)
        cv2.line(img, (int(coord2[0]), int(coord2[1])), (int(coord3[0]), int(coord3[1])), (10, 200, 10), 1)
        cv2.line(img, (int(coord3[0]), int(coord3[1])), (int(coord0[0]), int(coord0[1])), (200, 15, 0), 1)
        cv2.circle(img, (int(coord0[0]), int(coord0[1])), 2, (15, 15, 255), 2)  # red
        cv2.circle(img, (int(coord1[0]), int(coord1[1])), 2, (15, 255, 0), 2)  # green
        cv2.circle(img, (int(coord2[0]), int(coord2[1])), 2, (250, 250, 250), 2)  # white
        cv2.circle(img, (int(coord3[0]), int(coord3[1])), 2, (150, 150, 150), 2)  # gray
    cv2.imshow(window_name, img)


"""
Ultimately returns 4 coordinates (x,y) of a rectangle computed from its center, angle and width/height.
Order: Top left, top right, bottom right, bottom left.
"""
def F_get_corners_from_rectangle(center_x, center_y, angle, rect_width, rect_height):
    corners = np.array([[-rect_width / 2, -rect_height / 2],
                        [rect_width / 2, -rect_height / 2],
                        [rect_width / 2, rect_height / 2],
                        [-rect_width / 2, rect_height / 2]], dtype=np.float)
    center = np.array([center_x, center_y], dtype=np.float)
    angle_in_rad = angle * np.pi / 180.0
    r_z = np.array([[np.cos(angle_in_rad), -np.sin(angle_in_rad)],
                    [np.sin(angle_in_rad), np.cos(angle_in_rad)]])
    rotated_corners = corners @ r_z.T
    rotated_corners += center
    return rotated_corners

"""
Extract properties from single lines of Jacquard grasp files.
*_grasps.txt:
 a text file with the grasps annotations. Each line in the file is one grasp written as x;y;theta in degrees;opening;jaws size.
 Please note that all values are in image coordinates, so they are expressed in pixels, y is toward the bottom of the image (and therefore the angle is
  horizontally mirrored). When the position is the same on multiple consecutive rows, the first one corresponds to the grasp with the default jaws size of
  2 cm and the followings are just repetition of this grasp with different sizes.
"""
def F_extract_file(path_to_grasp_file, callback):
    with open(path_to_grasp_file,'r') as file:
        lines = file.readlines()

    rectangle_corners = []
    # interate lines
    for line in lines:
        split = line.split(';')

        #extract properties only for readability
        new_x_center = float(split[0]) * SCALE_FACTOR
        new_y_center = float(split[1]) * SCALE_FACTOR - 80
        theta = float(split[2])
        gripper_opening = float(split[3]) * SCALE_FACTOR
        gripper_jaws = float(split[4]) * SCALE_FACTOR
        rectangle_corners.append(callback(new_x_center, new_y_center, theta, gripper_opening, gripper_jaws))
    #print(rectangle_corners)
    return rectangle_corners

"""
Dumps list of grasps from one file to file.
path : string, path to save file
rectangle_corners_per_file: List of tuples with len(List[i]) == 4 representing 4 corner coordinates of one rectangle
"""
def F_write_to_cornell_grasps(path, rectangle_corners_per_file):
    with open(path, 'w') as f:
        for i in range(len(rectangle_corners_per_file)):
            rectangle = rectangle_corners_per_file[i]
            print(rectangle)
            f.write(
                "{} {} \n".format(round(rectangle[0][0]), round(rectangle[0][1]))
                + "{} {} \n".format(round(rectangle[1][0]), round(rectangle[1][1]))
                + "{} {} \n".format(round(rectangle[2][0]), round(rectangle[2][1]))
                + "{} {} \n".format(round(rectangle[3][0]), round(rectangle[3][1]))
            )

"""
Main loop.
Logging would be nice or at least print statements
"""
def run(source_path, target_path):
    counter = 0
    for root, dirs, files in os.walk(source_path):
        for filename in files:
            if('grasps.txt' in filename):
                split = filename.split('_')
                ident = "_".join([split[0], split[1]])

                #load images
                rgb = cv2.imread(os.path.join(root, ident + "_RGB.png"))
                depth = Image.open(os.path.join(root, ident + "_perfect_depth.tiff"))

                #resize to 640x640
                depth_resized = depth.resize((640, 640), Image.ANTIALIAS)
                rgb_resized = cv2.resize(rgb, (640, 640), 1, 1, cv2.INTER_CUBIC)

                #cut 80 pixels top and bottom from center
                cut_rgb = rgb_resized[ 80:560, 0:640]
                cut_depth = depth_resized.crop((0, 80, 640, 560))

                #write dat shit
                cv2.imwrite(os.path.join(target_path, "{}{}{}".format("pcd", str(counter).zfill(5), "r.png")), cut_rgb)
                cut_depth.save(os.path.join(target_path, "{}{}{}".format("pcd", str(counter).zfill(5), "d.tiff")))
                grasps = F_extract_file(os.path.join(root, filename), callback=F_get_corners_from_rectangle)
                F_write_to_cornell_grasps(target_path + "pcd" + str(counter).zfill(5) + "cpos.txt", grasps)

                # Visualize
                #visualize_grasps(cut_rgb, grasps, window_name='Grasps')
                #cv2.waitKey(0)
                counter += 1

def F_parse():
    parser = argparse.ArgumentParser(description='Arguments:')
    parser.add_argument('--s', action='store', type=str, help='Source path (path to Jacquard main folder)')
    parser.add_argument('--t', action='store', type=str, help='Target path (path to save new dataset). Info: If not accessible, program breaks!')

    return parser.parse_args()

# dis main
if __name__ == "__main__":
    args = F_parse()

    if(os.path.exists(args.t) and os.path.isdir(args.t)):
        source_p = args.s
        target_p = args.t

    # run dat shit
    run(source_p, target_p)

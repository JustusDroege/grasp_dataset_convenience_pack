import DataPoint
import matplotlib.pyplot as plt
import cv2
from typing import List
from random import randrange

#CONSTANTS
CIRCLE_RADIUS = 1
CIRCLE_COLORS = [(100,255,255), (255,255,100), (255,100,255), (100,100,100)]
LINE_THICKNESS = 1
LINE_COLORS = [(100,255,0), (0,255,100)]

def visualize_full(data : DataPoint, change_color=False, corner_radius=CIRCLE_RADIUS, corner_colors=CIRCLE_COLORS, 
                        line_thickness=LINE_THICKNESS, line_colors=LINE_COLORS):
    img = cv2.imread(data.color, cv2.IMREAD_UNCHANGED)
    # draw corners
    for i in range(len(data.rectangle_corners)):
        current = data.rectangle_corners[i]
        img = draw_shapes_on_image(img, current, corner_radius, corner_colors, line_thickness, line_colors)

    plt.imshow(img)
    plt.show()

def visualize_random(data : DataPoint, amount : int, change_color=False, corner_radius=CIRCLE_RADIUS, corner_colors=CIRCLE_COLORS, 
                        line_thickness=LINE_THICKNESS, line_colors=LINE_COLORS):
    
    img = cv2.imread(data.color, cv2.IMREAD_UNCHANGED)
    indices = []
    for i in range(amount):
        to_add = randrange(len(data.rectangle_corners))
        if(to_add not in indices): #only to prevent doubles
            indices.append(to_add)
    for i in indices:
        current = data.rectangle_corners[i]
        img = draw_shapes_on_image(img, current, corner_radius, corner_colors, line_thickness, line_colors)
        
    plt.imshow(img)
    plt.show()

def visualize_specific(data : DataPoint, indices : List, change_color=False, corner_radius=CIRCLE_RADIUS, corner_colors=CIRCLE_COLORS, 
                        line_thickness=LINE_THICKNESS, line_colors=LINE_COLORS):
    img = cv2.imread(data.color, cv2.IMREAD_UNCHANGED)
    for i in indices:
        if(i < len(data.rectangle_corners)):
            continue

        current = data.rectangle_corners[i]
        img = draw_shapes_on_image(img, current, corner_radius, corner_colors, line_thickness, line_colors)
        
    plt.imshow(img)
    plt.show()   
                
def draw_shapes_on_image(img, grasp, corner_radius, corner_colors, line_thickness, line_colors):
    cv2.line(img, tuple(grasp[0]), tuple(grasp[1]), line_colors[0], line_thickness)
    cv2.line(img, tuple(grasp[1]), tuple(grasp[2]), line_colors[1], line_thickness)
    cv2.line(img, tuple(grasp[2]), tuple(grasp[3]), line_colors[0], line_thickness)
    cv2.line(img, tuple(grasp[3]), tuple(grasp[0]), line_colors[1], line_thickness)

    cv2.circle(img, tuple(grasp[0]), corner_radius, corner_colors[0], 2)
    cv2.circle(img, tuple(grasp[1]), corner_radius, corner_colors[1], 2)
    cv2.circle(img, tuple(grasp[2]), corner_radius, corner_colors[2], 2)
    cv2.circle(img, tuple(grasp[3]), corner_radius, corner_colors[3], 2)
    
    return img  

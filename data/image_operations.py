#from .DataPoint import DataPoint
import matplotlib.pyplot as plt
import cv2
import os
from typing import List
from random import randrange
from data import Options
from data import enums

from data.enums import visiualization_option

#CONSTANTS
CIRCLE_RADIUS = 2
CIRCLE_COLORS = [(100,255,255), (255,255,100), (255,100,255), (100,100,100)]
LINE_THICKNESS = 2
LINE_COLORS = [(100,255,0), (0,255,100)]

def visualize_full(data, change_color=False, corner_radius=CIRCLE_RADIUS, corner_colors=CIRCLE_COLORS, 
                        line_thickness=LINE_THICKNESS, line_colors=LINE_COLORS):
    img = cv2.imread(data.color, cv2.IMREAD_UNCHANGED)
    # draw corners
    for i in range(len(data.rectangle_corners)):
        current = data.rectangle_corners[i]
        img = draw_shapes_on_image(img, current, corner_radius, corner_colors, line_thickness, line_colors)

    plt.imshow(img)
    plt.show()

def visualize_random(data, amount : int, change_color=False, corner_radius=CIRCLE_RADIUS, corner_colors=CIRCLE_COLORS, 
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

def visualize_specific(data, options):
    img = process_random(data, options)
        
    plt.imshow(img)
    plt.show()   

def viz(data, options):
    img = process_random(data, options)
    plt.imshow(img)
    plt.show()

def save(data, location : str, filename : str, options : Options):
    img = process_random(data, options)
    cv2.imwrite(os.path.join(location, filename + ".png"), img)

"""
Adds the visual annotations based on the options given.
"""
def process_random(data, options):
    img = cv2.imread(data.color, cv2.IMREAD_UNCHANGED)
    indices = []
    if(options.mode == visiualization_option.FULL):
        for i in range(len(data.rectangle_corners)):
            current = data.rectangle_corners[i]
            img = draw_shapes_on_image(img, current, corner_radius, corner_colors, line_thickness, line_colors)

    if(options.mode == visiualization_option.RANDOM):
        for i in range(options.amount):
            to_add = randrange(len(data.rectangle_corners))
            if(to_add not in indices): #only to prevent doubles
                indices.append(to_add)
        for i in indices:
            current = data.rectangle_corners[i]
            img = draw_shapes_on_image(img, current, options.circle_radius, options.circle_colors, options.line_thickness, options.line_colors)

    if(options.mode == visiualization_option.SPECIFIC):
        indices = options.indices
        for i in indices:
            if(i < len(data.rectangle_corners)):
                continue

            current = data.rectangle_corners[i]
            img = draw_shapes_on_image(img, current, corner_radius, corner_colors, line_thickness, line_colors)
    
    return img



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


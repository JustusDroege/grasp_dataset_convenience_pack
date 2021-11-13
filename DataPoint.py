from dataclasses import dataclass
from typing import List
import matplotlib.pyplot as plt
from enums import visiualization_option
import visualization

@dataclass
class DataPoint:
    def __init__(self, depth : str, color : str, grasps : str) -> None:
        self.depth = depth
        self.color = color
        self.grasps = grasps
        self.valid = (depth is not "" and color is not "" and grasps is not "")

        self.rectangle_corners = self.read_grasp_file(self.grasps)
        self.amount_grasps = len(self.rectangle_corners)

    def read_grasp_file(self, path_to_grasp_file):
        grasp_rectangles = []
        f = open(path_to_grasp_file, "r")
        raw = f.readlines()
        c = 0
        for i in range(0, len(raw), 4):
            current_grasp = []
            current_grasp.append(list(map(int, raw[i].split())))
            current_grasp.append(list(map(int, raw[i+1].split())))
            current_grasp.append(list(map(int, raw[i+2].split())))
            current_grasp.append(list(map(int, raw[i+3].split())))
            grasp_rectangles.append(current_grasp)
        return grasp_rectangles

    def visualize(self, option : visiualization_option, amount_grasps_to_display=1, grasps_to_display :List =[0]):
        if(option == visiualization_option.FULL):
            visualization.visualize_full(self)
        elif(option == visiualization_option.RANDOM):
            visualization.visualize_random(self, amount_grasps_to_display)
        elif(option == visiualization_option.SPECIFIC):
            visualization.visualize_specific(self, grasps_to_display)            

from dataclasses import dataclass
import os
from typing import List
import matplotlib.pyplot as plt

from data import image_operations
from .enums import visiualization_option
from . import image_operations
from .Options import Options

@dataclass
class DataPoint:
    def __init__(self, depth : str, color : str, grasps : str, digit : str) -> None:
        self.depth = depth
        self.color = color
        self.grasps = grasps
        self.digit = int(digit)
        self.valid = (depth is not "" and color is not "" and grasps is not "")

        self.rectangle_corners = self.read_grasp_file(self.grasps)
        self.amount_grasps = len(self.rectangle_corners)

        self.normpath = os.path.normpath(self.depth).split(os.sep)[-2:]

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

    def visualize(self, options : Options=Options()):
        image_operations.viz(self, options)

    def save(self, location : str=None, filename : str=None,options : Options=Options()):
        location = self.normpath if location is None else location
        filename = str(self.digit) if filename is None else filename
        if not (os.path.exists(location)):
            raise NotADirectoryError("Given save location is not a valid path!")
        image_operations.save(self, location, filename, options)

from dataclasses import dataclass

@dataclass
class DataPoint:
    def __init__(self, depth : str, color : str, grasps : str) -> None:
        self.depth = depth
        self.color = color
        self.grasps = grasps

        self.valid = (depth is not "" and color is not "" and grasps is not "")
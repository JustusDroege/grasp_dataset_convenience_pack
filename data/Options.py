from dataclasses import dataclass
from .enums import save_option, visiualization_option

@dataclass
class Options:
    def __init__(self, 
                    mode : visiualization_option=visiualization_option.RANDOM,
                    save_mode : save_option=save_option.RANDOM,
                    output_name="test",
                    amount : int=5,
                    indices=[1],
                    circle_radius : int=2,
                    line_thickness : int=2,
                    circle_colors=[(100,255,255), (255,255,100), (255,100,255), (100,100,100)],
                    line_colors=[(100,255,0), (0,255,100)]) -> None:
        self.mode = mode
        self.output_name=output_name
        self.amount=amount
        self.indices=indices
        self.circle_radius = circle_radius
        self.line_thickness = line_thickness
        self.circle_colors = circle_colors
        self.line_colors = line_colors
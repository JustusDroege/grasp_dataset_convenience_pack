from enum import Enum

class save_option(Enum):
    RANDOM = 0
    SPECIFIC = 1

class visiualization_option(Enum):
    FULL = 0
    RANDOM = 1
    SPECIFIC = 2

class jacquard_depth(Enum):
    STEREO = 0
    PERFECT = 1
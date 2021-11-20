from dataclasses import dataclass

@dataclass
class DataInfo:
    """
    Stores misc infos about a folder of a Dataset. 
    data_start: lowest data point number in folder
    data_end: highest " "
    prefix: prefix of dataset files, e.g. "rc"
    suffices: d: depth, c: color, g: grasp files
    """
    def __init__(self, data_start : int, data_end : int, zfill : int, prefix : str, suffix_d : str, suffix_c : str, suffix_g : str) -> None:
        self.data_start = data_start
        self.data_end = data_end
        self.zfill = zfill
        self.prefix = prefix
        
        # deoth image suffix
        self.suffix_d = suffix_d
        
        # color image suffix
        self.suffix_c = suffix_c

        #grasp file suffix
        self.suffix_g = suffix_g
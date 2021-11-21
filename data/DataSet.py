import os
import random
from typing import List
from data import DataPoint

from data.Options import Options
from .DataFolder import DataFolder
from .enums import save_option, visiualization_option

class Dataset:
    def __init__(self, location) -> None:
        if(location == "" or not os.path.exists):
            return
        
        self.path_to_main_folder = location
        
        # get tree info
        self.subfolders = self.get_subfolders()

    def get_subfolders(self) -> list:
        """
        Get subfolders of the dataset.
        Returns list with root path strings for each subfolder in the dataset.
        """
        data_folders = []
        misc = []
        for folder in os.listdir(self.path_to_main_folder):
            if not (os.path.isdir(os.path.join(self.path_to_main_folder, folder))):
                misc.append(os.path.join(self.path_to_main_folder, folder))
                continue
            print(f"Loading data at {os.path.join(self.path_to_main_folder, folder)}")
            data_folders.append(DataFolder(os.path.join(self.path_to_main_folder, folder)))
        if(len(misc) != 0):
            print(f"Found {len(misc)} non-folder objects.")
        return data_folders

    def print_folder_info(self) -> None:
        """
        Prints info about the instance.
        """
        print(f"##### Info #####")
        print(f"Location: {self.path_to_main_folder}")
        print(f"Distributed in {len(self.subfolders)} subfolders:")
        [print(f"{f.location}\n") for f in self.subfolders]

    def save_samples(self, amount : int=None, indices :List=None, save_location : str=None, options : Options=Options()
                     ):
        """
        Iterates through the subfolders and saves images to save_location:
        RANDOM: Randomly selects images to save.
        SPECIFIC: Saves specific image numbers.
        """
        amount = options.amount if amount is None else amount
        save_location = self.path_to_main_folder if save_location is None else save_location
        if not (os.path.exists(save_location)):
            raise NotADirectoryError("Given save location is not a valid path!")
        if(indices is not None):
            for i in range(len(indices)):
                dp_choice = self.find_datapoint(str(indices[i]).zfill(self.subfolders[0].info.zfill))
                if(dp_choice == 0): continue
                dp_choice.save(location=save_location, options=options)
        elif(indices is None and amount is not None):
            for i in range(amount):
                f_choice = random.choice(self.subfolders)
                dp_choice = random.choice(f_choice.datapoints)
                dp_choice.save(location=save_location, options=options)
    
    """
    O^2 algorithm quick and dirty return Datapoint to a given number.
    """
    def find_datapoint(self, digit : str) -> DataPoint:
        for i in range(len(self.subfolders)):
            tmp_sf = self.subfolders[i]
            tmp_zfill = self.subfolders[i].info.zfill
            for j in range(len(tmp_sf.datapoints)):  
                test = str(tmp_sf.datapoints[j].digit).zfill(tmp_zfill)
                if(str(tmp_sf.datapoints[j].digit).zfill(tmp_zfill) == digit):
                    return tmp_sf.datapoints[j]
        return 0

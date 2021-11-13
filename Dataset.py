import os
from Datafolder import DataFolder
import enums

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
        for folder in os.listdir(self.path_to_main_folder):
            print(f"Loading data at {os.path.join(self.path_to_main_folder, folder)}")
            data_folders.append(DataFolder(os.path.join(self.path_to_main_folder, folder)))
        return data_folders

    def print_folder_info(self) -> None:
        """
        Prints info about the instance.
        """
        print(f"##### Info #####")
        print(f"Location: {self.path_to_main_folder}")
        print(f"Distributed in {len(self.subfolders)} subfolders:")
        [print(f"{f.location}\n") for f in self.subfolders]

    def save_samples(save_option : enums.save_option, grasp_option : enums.visiualization_option, save_location :str):
        """
        Iterates through the subfolders and saves images to save_location:
        RANDOM: Randomly selects images to save.
        SPECIFIC: Saves specific image numbers.
        """
        if(save_option == enums.save_option.RANDOM):
            pass
        elif(save_option == enums.save_option.SPECIFIC):
            pass
        pass


            
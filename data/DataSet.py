import os
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

    def save_samples(self, save_option : save_option, grasp_option : visiualization_option, save_location : str,
                     samples_to_save : int =20, specific_to_save=[0,1,2,3,4,5]):
        """
        Iterates through the subfolders and saves images to save_location:
        RANDOM: Randomly selects images to save.
        SPECIFIC: Saves specific image numbers.
        """
        if not (os.path.exists(save_location)):
            raise NotADirectoryError("Given save location is not a valid path!")
        if(save_option == save_option.RANDOM):
            
            pass
        elif(save_option == save_option.SPECIFIC):
            pass
        pass


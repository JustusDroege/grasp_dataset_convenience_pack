import os
import Datafolder
import Dataset
from enum import Enum

class Option(Enum):
    RANDOM = 0
    SPECIFIC = 1

class Dataset:
    def __init__(self, location) -> None:
        if(location == "" or not os.path.exists):
            return
        
        self.path_to_main_folder = location
        
        # get tree info
        self.subfolders = self.GetSubfolders()

    def GetSubfolders(self) -> list:
        """Get subfolders of the dataset.

        Returns list with root path strings for each subfolder in the dataset.
        """
        data_folders = []
        for folder in os.listdir(self.path_to_main_folder):
            data_folders.append(Datafolder.Datafolder(os.path.join(self.path_to_main_folder, folder)))
        return data_folders

    def PrintInfo(self) -> None:
        """Prints info about the instance.
        """
        print(f"##### Info #####")
        print(f"Location: {self.path_to_main_folder}")
        print(f"Distributed in {len(self.subfolders)} subfolders:")
        [print(f"{f.location}\n") for f in self.subfolders]

    @staticmethod
    def Merge(data1 : Dataset) -> Dataset:
        return Dataset("")

    def Visualize(cls):
        print("visualize")
        pass

    def SaveOutput(Option : Option):
        pass


if __name__ == '__main__':
    data = Dataset("path")
            
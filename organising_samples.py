import os
import math


def get_list_files(path):
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return files


if __name__ == '__main__':
    dataset_path = './Processed_Data_copy'
    num_samples_per_subdirectory = 10

    suffixes = ['cpos.txt', 'd.tiff', 'r.png', 'l.png']
    files = get_list_files(dataset_path)

    # Group files into datapoints
    prefixes = []
    for file in files:
        prefix = file[:8]
        if prefix not in prefixes:
            prefixes.append(prefix)

    dir_counter = 0
    for i, prefix in enumerate(prefixes):
        dir = f"{dir_counter:05}"
        dir_path = os.path.join(dataset_path, dir)

        # create directory
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        # move files
        for suffix in suffixes:
            filename = f'{prefix}{suffix}'
            tmp_original = os.path.join(dataset_path, filename)
            tmp = os.path.join(dir_path, filename)
            if os.path.exists(tmp_original):
                os.rename(tmp_original, tmp)

        dir_counter = math.floor(i/num_samples_per_subdirectory)



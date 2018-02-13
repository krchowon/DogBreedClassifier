import os
import numpy as np

# This function takes as arguments:
#   file_map:               dictionary mapping files to folder name
#   path:                   string representing the path where files are mapped
#   file_suffix (optional)  string suffix of the file type
# And sorts all the files into folders
def partition_file(file_map, path, file_suffix=".jpg"):
    # 1) create the folders if not already created
    for v in file_map.values():
        # i) folder name:
        directory = path + "\\" + str(v)
        if not os.path.exists(directory):
            os.makedirs(directory)

    # 2) move files accordingly

    for file in os.listdir(path):
        if file.endswith(file_suffix):
            # i) retrieve id name of picture that maps to a folder
            file_id = file[:-len(file_suffix)]

            if file_id in file_map.keys():
                dest_folder = file_map[file_id]
                os.rename(path + "\\" + file,
                          path + "\\" + dest_folder + "\\" + file)
            else:
                print("[-W-]: A file, " + file + ", found that is not mapped to a folder.\n")


# This function takes as input
#   in_path_list:        list        a list of paths representing the super set of training data,
#   test_size:      float       0 to 1 proportion of full data set to split into testing
def train_test_split(file_map, in_path_list, dest_path, test_size, random_state=11, file_suffix=".jpg"):
    # 1) determine train test split:
    #   i) init split
    np.random.seed(random_state)
    file_name = list(file_map.keys())
    #   ii) Shuffle
    np.random.permutation(file_name)
    split_idx = int(np.floor(test_size * len(file_name)))

    #   iii) split
    valid = file_name[:split_idx]
    train = file_name[split_idx:]

    # 2) Move files to correct folders
    #   i) setup file structure
    train_path = dest_path + "\\" + "train\\"
    for folder in file_map.values():
        if not os.path.exists(train_path + "\\" + folder):
            os.makedirs(train_path + "\\" + folder)

    valid_path = dest_path + "\\" + "valid\\"
    for folder in file_map.values():
        if not os.path.exists(valid_path + "\\" + folder):
            os.makedirs(valid_path + "\\" + folder)

    #   ii) get the list of all files and add to the map
    path_map = {}
    for path in in_path_list:
        for folder in os.listdir(path):
            if os.path.isdir(path + "\\" + folder):
                for file in os.listdir(path + "\\" + folder):
                    if file.endswith(file_suffix):
                        path_map[file[:-len(file_suffix)]] = path + "\\" + folder
                    else:
                        print('Unexpected file suffix encountered on: ' + file)
            else:
                print('Unexpected file encountered while splitting directory')

    #   ii) Move Training Set
    #   todo: make sure it overrides if already present?
    for file in train:
        if file in path_map:
            os.rename(path_map[file] + "\\" + file + file_suffix,
                      train_path + "\\" + file_map[file] + "\\" + file + file_suffix)
        else:
            raise Exception('File map encountered that is not in path list: ' + file + file_suffix)

    #   iii) Move Validation Set
    for file in valid:
        if file in path_map:
            os.rename(path_map[file] + "\\" + file + file_suffix,
                      valid_path + "\\" + file_map[file] + "\\" + file + file_suffix)
        else:
            raise Exception('File map encountered that is not in path list: ' + file + file_suffix)

import os
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
            file_id = file[:-4]

            if file_id in file_map.keys():
                dest_folder = file_map[file_id]
                os.rename(path + "\\" + file,
                          path + "\\" + dest_folder + "\\" + file)
            else:
                print("A file, " + file + ", found that is not mapped to a folder.")




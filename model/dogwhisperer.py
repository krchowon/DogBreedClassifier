from model import utils
import pandas as pd
import os

class ImageClassifierData():

    @classmethod
    def from_csv(cls, csv_file, data_folder, test_folder):
        label_df = pd.read_csv(csv_file)

        breed_id = {row['id']:row['breed'] for i,row in label_df.iterrows()}

        # partition training data
        # utils.partition_file(file_map=breed_id, path=data_folder)

        # partition test data
        utils.partition_file(file_map=breed_id, path=test_folder)



if __name__ == "__main__":
    path = os.getcwd()

    label_csv = path+ r"\data\labels.csv"
    train_folder = path + r"\data\dogbreeds\train"
    valid_folder = path + r"\data\dogbreeds\test"


    icd = ImageClassifierData()

    icd.from_csv(csv_file=label_csv, data_folder=train_folder, test_folder=valid_folder)


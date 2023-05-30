## 废弃
import glob
import os

def ReName(path):
    baseName = os.path.basename(path)
    farther_dir = os.path.dirname(path)
    if baseName == "train":
        for file in glob.glob(path + '/all.csv'):
            os.rename(file,os.path.join(farther_dir,baseName + '.csv'))


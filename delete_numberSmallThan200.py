# 删除少于200的，这里没有表头
import glob
import pandas as pd
import os


def Delete_LengthSmallerThan200(path):

    for files in glob.glob(path + '/*.csv'):
        df = pd.read_csv(files,header=None) ##没有表头，所以加个 header=None
        length = len(df)

        if length < 200:
            os.remove(files)
        # print(files + "已完成")
    print("轨迹点少于200的删除")





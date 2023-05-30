# 这个函数给csv增加一列
import glob
import pandas as pd

def Exchange(path):  # 这个函数给csv增加一列
    #先给这些文件都加一列index，简写idx
    for files in glob.glob(path + '/*.csv'):
        df = pd.read_csv(files)
        order = ['LAT', 'LON', 'idx', 'SOG','COG']
        df = df[order]
        df.to_csv(files,index=None)
    print("交换顺序成功")
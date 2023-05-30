# 这个函数给csv增加一列
import glob
import pandas as pd

def AddIdx(path):  # 这个函数给csv增加一列
    i = 0
    #先给这些文件都加一列index，简写idx
    for files in glob.glob(path + '/*.csv'):
        df = pd.read_csv(files)
        df['idx'] = i
        order = ['BaseDateTime', 'LAT', 'LON',
                 'SOG','COG','MMSI', 'idx']
        df = df[order]
        df.to_csv(files,index=None)
        i += 1

#删除重复行之前，必须要加个表头
import glob
import pandas as pd
import shutil
import os



def Delete_ChongFuHang(path):
    for files in glob.glob(path + '/*.csv'):
        df = pd.read_csv(files)
        df.drop_duplicates(subset=['BaseDateTime'],keep='first',inplace=True)
        df.to_csv(files,index=None)
    print("根据时间删除重复数据已完成")

    

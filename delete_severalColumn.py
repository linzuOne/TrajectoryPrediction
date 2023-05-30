#删除不需要的列，这里是删除 BaseDateTime
import pandas as pd
import glob
import numpy as np

#path = 'E:\\shuju\\temp'
def deleteColumn(path):
    for files in glob.glob(path + '/*.csv'):
        df = pd.read_csv(files)
        df = df.drop(['BaseDateTime'],axis=1)
        df.to_csv(files,index=False)
    print("删除不必要的列，成功")
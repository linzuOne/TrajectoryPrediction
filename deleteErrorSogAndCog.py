import numpy as np
import pandas as pd
import glob

def deleteErrorSOG(path):
    for files in glob.glob(path + '/*.csv'):
        df = pd.read_csv(files)
        row_list = []
        for i in range(len(df)):
            if df['SOG'][i] < 0 or df['SOG'][i] > 50:
                row_list.append(i)

        df = df.drop(df.index[row_list])
        df.to_csv(files, index=None)
        print(files + "删除异常sog完成了")
    print("SOG部分完成了")


def ToCorrectErrorCOG(path):
    ## 这个函数将 cog 为负数的更正为 正数
    for files in glob.glob(path + '/*.csv'):
        df = pd.read_csv(files)
        for i in range(len(df)):
            if df['COG'][i] < 0 :
                df['COG'][i] = df['COG'][i] + 409.6

        df.to_csv(files, index=None)
        print(files + "将cog改为正数完成了")
    print("COG负数改正数完成了")

def deleteErrorCOG(path):
    for files in glob.glob(path + '/*.csv'):
        df = pd.read_csv(files)
        row_list = []
        for i in range(len(df)):
            if df['COG'][i] < 0 or df['COG'][i] > 360:
                row_list.append(i)

        df = df.drop(df.index[row_list])
        df.to_csv(files, index=None)
        print(files + "删除异常cog完成了")
    print("COG部分完成了")


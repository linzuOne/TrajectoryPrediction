#删除括号中的五列，以及船舶类型为括号中的那些，这些是小船或者非船舶
import pandas as pd
import glob
import numpy as np

def delete_small(path):

    for files in glob.glob(path + '/*.csv'):
        df = pd.read_csv(files)
        df.drop(columns=["Heading","VesselName","CallSign","Draft","Cargo"],inplace=True)
        ## 上面将 heading等 5列删除，下面将 vesseltype标号在下面这些数字范围内的都删除，这些表示小船
        row_indexs = df[df.VesselType.isin([0,1,2,3,4,5,6,7,8,9,10,11,12,
                                               13,14,15,16,17,18,19,20,21,22,23,25,26,27,28,
                                               29,33,34,36,37,50,51,53,55,58,59,1019])].index
        df.drop(row_indexs,inplace=True)
        df.to_csv(files,index=False)
    print("删除vesseltype小船，成功")


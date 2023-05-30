##经纬度各自的差都在0.2以内，删除轨迹
import shutil
import os
import pandas as pd
import glob
import numpy as np

def deleteDifference_02(path):
    for file in glob.glob(path + '/*.csv'):
        df = pd.read_csv(file).iloc[:,2:4].values

        list1 = df[:, 0]    #df[:,0]是纬度   df[[:,1]是经度
        listlow1, listhigh1 = np.percentile(list1, [0, 100])

        list2 = df[:, 1]  # df[:,0]是纬度   df[[:,1]是经度
        listlow2, listhigh2 = np.percentile(list2, [0, 100])


        if listhigh1 - listlow1 <= 0.2 and listhigh2 - listlow2 <= 0.2:
            os.remove(file)


        print(file + "完成了")

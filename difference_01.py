##经纬度随便哪一个差了0.1度，就去除掉轨迹
import shutil
import os
import pandas as pd
import glob
import numpy as np

def Difference_01(path):

    small_range = os.path.join(path, "航行范围小于0.1")
    folder = os.path.exists(small_range)
    if not folder:
        os.makedirs(small_range)
    else:
        pass

    for file in glob.glob(path + '/*.csv'):
        df = pd.read_csv(file).iloc[:,2:4].values
        flag = 0
        for i in range(2):   #df表示只读了两列数据
            list = df[:, i]    #df[:,0]是纬度   df[[:,1]是经度
            listlow, listhigh = np.percentile(list, [0, 100])

            if listhigh - listlow < 0.1:
                os.remove(file)
                flag = 1
                break

        if flag == 0:
            pass

        print(file + "完成了")
    return small_range

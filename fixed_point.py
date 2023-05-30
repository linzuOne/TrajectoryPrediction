## 获取固定长度的轨迹，例如获取每条轨迹都是50个点的轨迹集合、每条轨迹都是100个点的轨迹集合

import pandas as pd
import numpy as np
import os
import glob

def obtain_fixed_points(want_num, path):
    # want_num = 300
    # path = 'E:\\data_And_model\\data\\三百以上\\train\\已按6小时分割\\Interpolation'
    path1 = os.path.join(path, "每条轨迹取{}个点".format(want_num))

    folder = os.path.exists(path1)
    if not folder:
        os.makedirs(path1)
    else:
        pass


    for files in glob.glob(path + '/*.csv'):
        df = pd.read_csv(files)
        length_of_df = len(df)
        if length_of_df < want_num:
            continue

        front = os.path.basename(files)
        jiequ = os.path.splitext(front)[0]

        csv_list = []
        csv_list.append(df.iloc[0:want_num, :])
        newcsv = pd.DataFrame(np.row_stack(csv_list))
        csv_list.clear()
        savepath = path1 + "\\" + jiequ  + ".csv"
        newcsv.to_csv(savepath, header=False, index=False)



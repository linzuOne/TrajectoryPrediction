##经纬度各自的差都在0.2以内，删除轨迹
import shutil
import os
import pandas as pd
import glob
import numpy as np

path = 'E:\\shuju\\2017\\解压后\\04\\AfterMerge\\没有不同的IMO\\大型船舶\\已按时间分割\\超过10分钟就分割\\2'

small_range = os.path.join(path, "继续清洗——小")
folder = os.path.exists(small_range)
if not folder:
    os.makedirs(small_range)
else:
    pass

large_range = os.path.join(path,"继续清洗——大")
folder1 = os.path.exists(large_range)
if not folder1:
    os.makedirs(large_range)
else:
    pass

for file in glob.glob(path + '/*.csv'):
    df = pd.read_csv(file).iloc[:,2:4].values

    list1 = df[:, 0]    #df[:,0]是纬度   df[[:,1]是经度
    listlow1, listhigh1 = np.percentile(list1, [0, 100])

    list2 = df[:, 1]  # df[:,0]是纬度   df[[:,1]是经度
    listlow2, listhigh2 = np.percentile(list2, [0, 100])


    if listhigh1 - listlow1 < 0.2 and listhigh2 - listlow2 < 0.2:
        shutil.move(file,small_range)

    else:
        shutil.move(file,large_range)

    print(file + "完成了")

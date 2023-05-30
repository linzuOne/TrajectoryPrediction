import pandas as pd
import datetime
import time
import os
import shutil
import glob
import numpy as np

# path = 'E:\\shuju\\temp\\temp'
def splitByTime(path):
    path1 = os.path.join(path, "已按6小时分割")
    folder = os.path.exists(path1)
    if not folder:
        os.makedirs(path1)
    else:
        pass

    path2 = os.path.join(path, "已经处理好")
    folder2 = os.path.exists(path2)
    if not folder2:
        os.makedirs(path2)
    else:
        pass

    for files in glob.glob(path + '/*.csv'):
        print("现在处理的文件：   ",files)
        df = pd.read_csv(files)
        length = len(df)
        front = os.path.basename(files)
        jiequ = os.path.splitext(front)[0]

        k = 0

        count = 0
        while (k < length - 1):
            for i in range(k, length):
                value = df['BaseDateTime'][i]
                d1 = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
                sixhours = datetime.timedelta(hours=6)
                newtime = d1 + sixhours
                csv_list = []

                for j in range(i + 1, length):
                    value1 = df['BaseDateTime'][j]
                    d2 = datetime.datetime.strptime(value1, "%Y-%m-%dT%H:%M:%S")
                    if d2 <= newtime and j != length - 1:
                        continue

                    else:
                        if d2 > newtime:
                            csv_list.append(df.iloc[i:j, :])

                        if d2 < newtime and j == length - 1:
                            csv_list.append(df.iloc[i:j + 1, :])

                        newcsv = pd.DataFrame(np.row_stack(csv_list))
                        csv_list.clear()
                        count += 1
                        savepath = path1 + "\\" + jiequ + "__" + str(count) + ".csv"
                        newcsv.to_csv(savepath, header=False, index=False)
                        k = j
                        break

                break
        print(files + "文件已经完成")
        shutil.move(files,path2)
    print("按小时分段已完成")
    return path1

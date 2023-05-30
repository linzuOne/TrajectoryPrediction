#两个相邻点时间差30分钟时，就断开变成两截
import pandas as pd
import datetime
import time
import os
import shutil
import glob
import numpy as np

def splitByTime(path):
    path1 = os.path.join(path, "超过30分钟就分割")
    folder = os.path.exists(path1)
    if not folder:
        os.makedirs(path1)
    else:
        pass

    for files in glob.glob(path + '/*.csv'):
        df = pd.read_csv(files)
        length = len(df)
        front = os.path.basename(files)
        jiequ = os.path.splitext(front)[0]

        count = 0
        j = 0
        csv_list = []

        for i in range(length-1):
            datetime1 = df['BaseDateTime'][i]
            datetime1 = time.strptime(datetime1, "%Y-%m-%dT%H:%M:%S")
            datetime1 = float(time.mktime(datetime1))  # 将时间戳转为秒

            datetime2 = df['BaseDateTime'][i + 1]
            datetime2 = time.strptime(datetime2, "%Y-%m-%dT%H:%M:%S")
            datetime2 = float(time.mktime(datetime2))  # 将时间戳转为秒

            if datetime2 - datetime1 < 1800  and i != length - 2 :
                continue

            if datetime2 - datetime1 >= 1800:
                csv_list.append(df.iloc[j:i+1, :])
                j = i + 1

            if i == length - 2:
                datetime_end = df['BaseDateTime'][length - 1]   ## 这个是最后一个
                datetime_end = time.strptime(datetime_end, "%Y-%m-%dT%H:%M:%S")
                datetime_end = float(time.mktime(datetime_end))  # 将时间戳转为秒

                datetime_penult = df['BaseDateTime'][i]     ## 这个是倒数第二个
                datetime_penult = time.strptime(datetime_penult, "%Y-%m-%dT%H:%M:%S")
                datetime_penult = float(time.mktime(datetime_penult))  # 将时间戳转为秒

                if datetime_end - datetime_penult < 1800:
                    csv_list.append(df.iloc[j:length,:])
                else:
                    csv_list.append(df.iloc[j:length-1, :])   ## 也就是最后一个舍弃掉

            newcsv = pd.DataFrame(np.row_stack(csv_list))
            csv_list.clear()
            count += 1
            savepath = path1 + "\\" + jiequ + "__" + str(count) + ".csv"
            newcsv.to_csv(savepath, header=False, index=False)

        # print(files + "文件已经完成")
    return path1
    print("按30分钟分段已完成")
# 将连续3个以上速度小于等于8的删除
import glob
import pandas as pd
import os
import shutil

def delete_3_8_SOG(path):
    row_list = []
    for files in glob.glob(path + '/*.csv'):
        df = pd.read_csv(files)
        length = len(df)

        k = 0
        flag = 0
        while (k < length):
            if flag == 1:
                break
            for i in range(k, length):
                if i == length - 1:
                    flag = 1
                    break
                if df['SOG'][i] <= 8:
                    for j in range(i + 1, length):
                        if df['SOG'][j] > 8:
                            if j - i > 3:
                                for deleteROW in range(i, j):
                                    row_list.append(deleteROW)
                                # print(row_list)
                                df = df.drop(row_list)
                                row_list = []
                                k = j + 1

                                break
                            else:
                                k = j + 1
                                break
                        if j == length - 1:
                            flag = 1
                            if j - i >= 3:
                                for ROW in range(i, j + 1):
                                    row_list.append(ROW)
                                df = df.drop(row_list)
                                row_list.clear()
                            break
                    # print("第二个break")
                    break
                else:
                    k += 1
                    break
        df.to_csv(files, index=False)
    print("删除连续3个以上速度小于等于8的点，成功")
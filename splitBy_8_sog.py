##  将速度异常值改为正常值之后，再按速度切割
## 将 速度值 8 作为阈值
import pandas as pd
import glob
import shutil
import numpy as np
import os

def SplitBy_8_Sog(path):
    path1 = os.path.join(path, "按照速度分段")
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

    for file in glob.glob(path + '/*.csv'):
        df = pd.read_csv(file)
        new_csv_list = []
        count = 0
        s = 0
        front = os.path.basename(file)
        jiequ = os.path.splitext(front)[0]
        flag = 0
        flag2 = 0
        flag3 = 0
        print("len:    ",len(df),end="  ")
        print(file)
        while(s < len(df)):
            # print("s:    ",s)
            if len(df) - s  < 10:  ## 到轨迹末尾的时候，有可能出现 df['SOG'][j] 、df['SOG'][k]超出范围的情况，所以如果小于10，后面直接不要了
                break
            for i in range(s,len(df)):
                if df['SOG'][i] <= 8 and i != len(df) - 2 and i != len(df) - 1 and df['SOG'][i+1] <= 8:
                    for j in range(i+2,len(df)):
                        if df['SOG'][j] > 8  and j != len(df)-2  and j != len(df) - 1 and df['SOG'][j+1] > 8 : #如果后面一直没有大于 1 的，则去else中
                            flag2 = 1
                            for k in range(j+2,len(df)):
                                # print("k:    ",k)
                                if df['SOG'][k] <= 8  and k != len(df) - 1 and df['SOG'][k+1] <= 8:
                                    flag3 = 1
                                    if i == 0 :
                                        new_csv_list.append(df.iloc[i:k+2, :])
                                        newcsv = pd.DataFrame(np.row_stack(new_csv_list))
                                        new_csv_list.clear()
                                        count += 1
                                        savepath = path1 + "\\" + jiequ + "__" + str(count) + ".csv"
                                        newcsv.to_csv(savepath, header=False, index=False)
                                        s = k
                                        flag = 1
                                        break

                                    if i != 0:
                                        if flag == 0:
                                            new_csv_list.append(df.iloc[0:i+2,:])
                                            newcsv = pd.DataFrame(np.row_stack(new_csv_list))
                                            new_csv_list.clear()
                                            savepath = path1 + "\\" + jiequ + "__" + str(count) + ".csv"
                                            newcsv.to_csv(savepath, header=False, index=False)
                                            flag = 1

                                        new_csv_list.append(df.iloc[i:k+2, :])
                                        newcsv = pd.DataFrame(np.row_stack(new_csv_list))
                                        new_csv_list.clear()
                                        count += 1
                                        savepath = path1 + "\\" + jiequ + "__" + str(count) + ".csv"
                                        newcsv.to_csv(savepath, header=False, index=False)
                                        s = k
                                        break

                                elif df['SOG'][k] <= 8 and k == len(df) - 1:
                                    new_csv_list.append(df.iloc[i:k + 1, :])
                                    newcsv = pd.DataFrame(np.row_stack(new_csv_list))
                                    new_csv_list.clear()
                                    count += 1
                                    savepath = path1 + "\\" + jiequ + "__" + str(count) + ".csv"
                                    newcsv.to_csv(savepath, header=False, index=False)
                                    s = k
                                    break

                                else:
                                    if k != len(df) - 1:
                                        continue
                                    else:
                                        print("没有小于 8 的 k")
                                        # shutil.move(file, path2)
                                        if i != 0:  ## 2 2  2 2 2 2 0 0 0 0 0 0  2 2 2 2 2 2 的情况下
                                            if flag3 == 0:
                                                new_csv_list.append(df.iloc[0:i + 2, :])
                                                newcsv = pd.DataFrame(np.row_stack(new_csv_list))
                                                new_csv_list.clear()
                                                count += 1
                                                savepath = path1 + "\\" + jiequ + "__" + str(count) + ".csv"
                                                newcsv.to_csv(savepath, header=False, index=False)

                                        new_csv_list.append(df.iloc[i:k + 1, :])
                                        newcsv = pd.DataFrame(np.row_stack(new_csv_list))
                                        new_csv_list.clear()
                                        count += 1
                                        savepath = path1 + "\\" + jiequ + "__" + str(count) + ".csv"
                                        newcsv.to_csv(savepath, header=False, index=False)
                                        s = k + 1
                                        break

                            break

                        # elif df['SOG'][j] > 1 and j == len(df) - 2:
                        elif df['SOG'][j] > 8 and (j == len(df) - 2 or j == len(df) - 1):
                            #下面这里注释可以打开，打开之后最后一部分会被读取写入到csv中
                            # new_csv_list.append(df.iloc[i:j + 2, :])
                            # newcsv = pd.DataFrame(np.row_stack(new_csv_list))
                            # new_csv_list.clear()
                            # count += 1
                            # savepath = path1 + "\\" + jiequ + "__" + str(count) + ".csv"
                            # newcsv.to_csv(savepath, header=False, index=False)
                            s = j + 1
                            break

                        ## 整条轨迹没有大于 1 的
                        else:
                            if j != len(df) - 1:
                                continue
                            else:
                                print("没有大于8的")
                                if i != 0:  ## 在 i 不等于 0 ， i 后面的 数据都小于等于 1 的情况下
                                    if flag2 == 0:
                                        new_csv_list.append(df.iloc[0:i + 2, :])
                                        newcsv = pd.DataFrame(np.row_stack(new_csv_list))
                                        new_csv_list.clear()
                                        count += 1
                                        savepath = path1 + "\\" + jiequ + "__" + str(count) + ".csv"
                                        newcsv.to_csv(savepath, header=False, index=False)
                                s = j + 1
                                break

                    break

                # elif df['SOG'][i] <= 1 and i == len(df) - 2:
                #     print("倒数第二个小于 1")
                #     break
                #如果全都大于 1
                else:
                    if i != len(df) - 1:
                        continue
                    else:
                        print("全都大于8")
                        # shutil.move(file, path3)  ## 整条轨迹都大于 1
                        new_csv_list.append(df.iloc[0:len(df), :])
                        newcsv = pd.DataFrame(np.row_stack(new_csv_list))
                        new_csv_list.clear()
                        count += 1
                        savepath = path1 + "\\" + jiequ + "__" + str(count) + ".csv"
                        newcsv.to_csv(savepath, header=False, index=False)
                        s = i + 1
                        break

        shutil.move(file,path2)
    return path1

import shutil
import os
import numpy as np
import pandas as pd
import glob
import random

def tiqu(path):

    path1 = os.path.join(path,"提取mmsi之后")
    folder = os.path.exists(path1)
    if not folder:
        os.makedirs(path1)
    else:
        pass

    path2 = os.path.join(path, "已处理好")
    folder = os.path.exists(path2)
    if not folder:
        os.makedirs(path2)
    else:
        pass

    for files in glob.glob(path + '/*.csv'):
        mycsv = pd.read_csv(files)
        #print(mycsv)
        #print(len(mycsv))
        k = 0
        flag = 1
        while(flag):
            if k == len(mycsv) -1 :
                #print(files + "这个文件处理结束")
                break
            for i in range(k, len(mycsv)):
                csv_list = []
                firstmmsi = str(mycsv['MMSI'][i])
                for j in range(i,len(mycsv)):
                    if str(mycsv['MMSI'][j]) == firstmmsi:
                        if j == len(mycsv) - 1 :
                            k = j
                            csv_list.append(mycsv.iloc[i:j + 1, :])
                        else:
                            continue
                    else:
                        
                        csv_list.append(mycsv.iloc[i:j,:])
                        k = j
    
                    #print(csv_list)
                    
                    newcsv = pd.DataFrame(np.row_stack(csv_list))
                    csv_list.clear()
                    
                    rand1 = str(random.randint(10000,1000000000))
                    rand2 = str(random.randint(10000,1000000000))
                    rand = "__" + rand1 + "__" + rand2
                    #从多个csv中必然会提取出相同mmsi号的，必然文件名会冲突（都是mmsi）
                    #所以加两个随机数
                
                    oldpath = path + "\\" + firstmmsi + rand + '.csv'
                    savepath = path1 + "\\" + firstmmsi + rand + '.csv'
                    newcsv.to_csv(oldpath,header=False,index=False)
                    shutil.move(oldpath,savepath)
    
                    break
                break
        shutil.move(files,path2)
    print("提取mmsi成功")        
    return path1
            




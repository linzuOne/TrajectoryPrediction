#将连续5个以上速度小于0.5的删除
import glob
import pandas as pd
import os
import shutil

#path = 'E:\\shuju\\temp\\temp'
def delete5SOG(path):
    row_list = []
    for files in glob.glob(path + '/*.csv'):
        df = pd.read_csv(files)
        length = len(df)
        #print(length)
        #print("上面是长度")
        #print("++++++++++++++++++++++")
        k = 0
        flag = 0
        while(k < length):
            #print("回来了")
            if flag == 1:
                #print("ok")
                break
            for i in range(k,length):
                #print("又进来了")
                if i == length - 1:
                    flag = 1
                    break
                if df['SOG'][i] < 0.5:
                    #print("下面是i值",end="")
    
                    #print(i)
                    #print("这里是sog小于0.5")
                    for j in range(i+1,length):
                        if df['SOG'][j] > 0.5:
                            #print("这里是sog大于0.5")
                            if j-i > 5:
                                for deleteROW in range(i,j):
                                    row_list.append(deleteROW)
                                #print(row_list)
                                df = df.drop(row_list)
                                row_list = []
                                k = j + 1
                                #print("这里是结尾",end=" ")
                                #print("此时的j", end=" ")
                                #print(j)
                                #print("=====================")
                                #print("此时的k",end=" ")
                                #print(k)
                                break
                            else:
                                k = j + 1
                                break
                        if j == length - 1:
                            flag = 1
                            if j-i >= 5:
                                for ROW in range(i,j+1):
                                    row_list.append(ROW)
                                df = df.drop(row_list)
                                row_list.clear()
                            break
                    #print("第二个break")
                    break
                else:
                    k += 1
                    #print("末尾的k值",end=" ")
                    #print(k)
                    break
        df.to_csv(files,index=False)
    print("删除连续5个以上速度小于0.5的点，成功")
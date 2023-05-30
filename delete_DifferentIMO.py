#将相同mmsi，不同imo以及imo为0的都移动到对应文件夹中
import pandas as pd
import glob
import numpy as np
import shutil
import os

#path = 'E:\\shuju\\temp'
def deleteIMO(path):
    OnlyOneIMO = os.path.join(path,"没有不同的IMO")    #先生成一个文件夹
    folder = os.path.exists(OnlyOneIMO)   #判断是否存在这个文件夹，没有则创建，有则pass
    if not folder:
        os.makedirs(OnlyOneIMO)
    else:
        pass
    
    #上面文件夹存放的文件，每个都只包含一个imo，下面创建的文件夹，里面的文件都包含多个imo
    MoreThanONeIMO = os.path.join(path,"超过一个imo")
    folder1 = os.path.exists(MoreThanONeIMO)
    if not folder1:
        os.makedirs(MoreThanONeIMO)
    else:
        pass
    
    #当imo处为空白时，移到下面这里去
    NoIMO = os.path.join(path,"imo为空白")
    folder2 = os.path.exists(NoIMO)
    if not folder2:
        os.makedirs(NoIMO)
    else:
        pass
    
    count = 0
    file_num = sum([os.path.isfile(listx) for listx in os.listdir(path)])-3  #获取文件数目
    #print(file_num)
    #print("上面是文件数目,减去创建的3个文件夹之后的数目")
    
    for files in glob.glob(path + '/*.csv'):
        df = pd.read_csv(files)
        basename = os.path.basename(files)   #这行代码意为获取文件名
        # filename = basename.split('.')[0]
            # print(df.VesselType.value_counts())
            # print("==================")
            # # print(df.VesselType.values)
            # print(len(df.VesselType.value_counts()))
            # # if df.VesselType.value_counts() :
            # #     print("true")
            # if len(df.VesselType.value_counts()) >=2:
            #     print(df.VesselType.value_counts()[1:].index[0])
            #     print(type(df.VesselType.value_counts()[1:].index))
        #print(df.IMO.value_counts(),end="")  #数组形式获取IMO值 以及 对应的数量
        #print("这里是第一处,file是",end=" ")
        #print(files)
        IMOnumber_list = []
        howmanyIMO = len(df.IMO.value_counts())
        #print(howmanyIMO)
        
    
        if howmanyIMO >=2:
            # print(df.IMO.values) 这个输出的是所有的imo组成的数组
            for i in range(0,howmanyIMO):
                # print(df.IMO.value_counts()[i:i+1].index[0],end="")
                #print(df.IMO.value_counts()[i:i+1].index[0])
                IMOnumber_list.append(df.IMO.value_counts()[i:i+1].index[0])
            #如果有超过2个imo，上面这个for循环就是将所有的imo号都添加到IMOnumber_list列表中
            shutil.move(files,os.path.join(MoreThanONeIMO,basename))
        elif howmanyIMO == 0:
            shutil.move(files, os.path.join(NoIMO,basename))
    
        else:
            shutil.move(files, os.path.join(OnlyOneIMO,basename))
        count += 1
        #print(count)
        #print("========================================")
    
    print("删除不同imo已完成")    
    return OnlyOneIMO
       




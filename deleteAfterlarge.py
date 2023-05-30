# 将多于9位的删除
import pandas as pd
import glob
#path = 'E:\shuju\\2017\解压后\\01\\1月份拆分之后'
def afterlargeTosmall(path):
    for files in glob.glob(path + '/*.csv'):
    
    # file = 'E:\shuju\\temp\\2017_0.csv'
        data = pd.read_csv(files)
        #print(files)
        #print(len(data))
        for i in range(0, len(data)):
            # print(len(str(data['MMSI'][i])))
            if len(str(data['MMSI'][i])) == 9:
                #print(files + "从大到小，删除长度多于9的任务已完成")
                break            
            if len(str(data['MMSI'][i])) > 9:
                data.drop(i, inplace=True)
                #print(i)
                data.to_csv(files, index=None)
    
                if len(str(data['MMSI'][i + 1])) == 9:
                    #print(files + '已删除位数多于9的')
                    break
    print("删除长度大于9的已成功")




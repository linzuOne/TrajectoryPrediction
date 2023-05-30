#给csv添加表头，这是已经去除了那些用不到的列之后的表头
import pandas as pd
import glob
# filename = 'E:\shuju\\temp\\2018.csv'
#path = 'E:\shuju\\2017\解压后\\01\\1月份拆分之后的'

def AddoneLine2(path):

    for file in glob.glob(path + '/*.csv'):
        #print(file + "正在处理中")
        df = pd.read_csv(file,encoding="UTF-8")
        # print(df.iloc[[0],[0]].values[0][0])
        #print(df.columns.values[0])
        if df.columns.values[0] == "MMSI":
            #print("yes")
            #print(file + "未处理")
            continue
    
        else:
            #print("no")
            df = pd.read_csv(file, header=None, names=['MMSI', 'BaseDateTime', 'LAT', 'LON','SOG',
                                                       'COG','IMO','VesselType','Status',
                                                       'Length','Width'])
            df.to_csv(file,index=None)
            #print(file + "已添加表头2")
    print("添加表头2已成功")
    
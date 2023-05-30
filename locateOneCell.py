#定位某一单元格 df.iloc[i,j] 表示第 i 行，第 j 列 那个单元格的数据
#取 ship_num 艘船舶，同时规定了字段类型

import pandas as pd
file = 'E:\\shuju\\测试集.csv'

df = pd.read_csv(file,header=None, dtype={"idx":int, "MMSI":int,
                                          "BaseDateTime":str,"LAT":float,
                                          "LON":float, "SOG":float,
                                          "COG":float,"IMO":str,
                                          "VesselType":int,"Status":str,
                                          "Length":float,"Width":float})


ship_num = int(df.iloc[len(df)-1,0] / 4)
for i in range(len(df)):
    if df.iloc[i,0] == ship_num:
        df = df.iloc[:i-1,:]
        break

df.to_csv(file,index=None)
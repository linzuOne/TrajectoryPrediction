#将文件按时间排序
import pandas as pd
import glob
#path = 'E:\shuju\\2017\解压后\\01\\1月份拆分之后'
def timesort(path):
    for files in glob.glob(path + '/*.csv'):
        #下面这里先添加表头
        #df = pd.read_csv(file, header=None, names=['MMSI', 'BaseDateTime', 'LAT', 'LON','SOG',
                                                           #'COG','IMO','VesselType','Status',
                                                           #'Length','Width'])
        #df.to_csv(file,index=None)  
        #上面先添加表头
        df = pd.read_csv(files)
        data = df.sort_values(by="BaseDateTime", ascending=True)
        data.to_csv(files, mode='w+', index=False)
    print("按时间从小到大排序已完成")
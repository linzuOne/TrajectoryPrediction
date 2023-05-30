#将csv从大到小排序
import pandas as pd
import glob
#path = 'E:\shuju\\2017\解压后\\01\\1月份拆分之后'
def tosmallsort(path):
    for files in glob.glob(path + '/*.csv'):
        df = pd.read_csv(files)
        data = df.sort_values(by="MMSI", ascending=False)
        data.to_csv(files, mode='w+', index=False)
    print("从大到小排序已完成")
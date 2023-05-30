## 删除表头，先读取，再写入就好了
import glob
import pandas as pd

def delete_first_Line(path):
    for files in glob.glob(path + '/*.csv'):
        df = pd.read_csv(files)
        if df.columns.values[0] == "LAT":
            df.to_csv(files,header=None,index=None)


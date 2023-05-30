# 删除少于200的，有表头
import glob
import pandas as pd
import os

def Delete_ShorterThan200(path):

    ##==============================================
    # path1 = os.path.join(path, "小于200")
    # folder = os.path.exists(path1)
    # if not folder:
    #     os.makedirs(path1)
    # else:
    #     pass
    ##===============================================

    for files in glob.glob(path + '/*.csv'):
        df = pd.read_csv(files)  ##有表头
        length = len(df)

        if length < 200:
            os.remove(files)
            # shutil.move(files,path1)
    print("轨迹点少于200的删除")





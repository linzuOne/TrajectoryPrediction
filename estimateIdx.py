## 判断 idx 有没有按顺序排，确保是从 0 开始 递增  00000 11111 2222222 这样 而不是 00000 2222222 11111
## 这个代码最后手动执行一下
import sys
import pandas as pd
import glob

def IdxSortError(path):
    flag = 0

    class idxError(Exception):
        pass

    for files in glob.glob(path + '/*.csv'):
        df = pd.read_csv(files)
        for i in range(len(df) - 1):
            try:
                if int(df['idx'][i + 1]) < int(df['idx'][i]):
                    print("此时的 i ： ", i)
                    flag = 1
                    raise idxError(files + "  idx排序错误")
            except idxError as e:
                print(e)

            else:
                pass

            if flag == 1:
                sys.exit("idx 排序出错，中断程序")

    print("idx 排序没有问题")
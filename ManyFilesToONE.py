# 这个函数是将多个文件合成一个用于训练
import os
import shutil

import pandas as pd

def ManyToOneFile(path,trace):
    train_or_test = os.path.basename(trace)
    trace_father = os.path.dirname(trace)
    file_list = os.listdir(path)
    save_file_name = train_or_test + '.csv'
    df = pd.read_csv(path + '\\' + file_list[0])  # 编码默认UTF-8，若乱码自行更改
    df.to_csv(path + '\\' + save_file_name, encoding="utf_8_sig", index=None)
    for i in range(1, len(file_list)):
        df = pd.read_csv(path + '\\' + file_list[i])
        df.to_csv(path + '\\' + save_file_name, encoding="utf_8_sig", index=None, header=False, mode='a+')

    shutil.move(path + '\\' + save_file_name, trace_father + '\\' + save_file_name)

    print("将所有文件全部合成为一个文件，已完成，并已将合成的文件移走到 data 文件夹下面")


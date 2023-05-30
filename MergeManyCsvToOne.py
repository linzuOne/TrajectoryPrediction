import pandas as pd
import os
import glob

Folder_Path = r'E:\\shuju\\训练'
def AddIdx(path):  # 这个函数给csv增加一列
    i = 0
    #先给这些文件都加一列index，简写idx
    for files in glob.glob(path + '/*.csv'):
        df = pd.read_csv(files)
        df['idx'] = i
        order = ['idx', 'MMSI', 'BaseDateTime', 'LAT', 'LON',
                 'SOG','COG','IMO','VesselType','Status',
                 'Length','Width']
        df = df[order]
        df.to_csv(files,index=None)
        i += 1

def ManyToOneFile(path):
    # OnlyOne = os.path.join(path, "将所有文件合成一个文件")  # 先生成一个文件夹
    # folder = os.path.exists(OnlyOne)  # 判断是否存在这个文件夹，没有则创建，有则pass
    # if not folder:
    #     os.makedirs(OnlyOne)
    # else:
    #     pass
    #

    file_list = os.listdir(path)
    save_file_name = 'all.csv'
    df = pd.read_csv(path + '\\' + file_list[0])  # 编码默认UTF-8，若乱码自行更改
    df.to_csv(path + '\\' + save_file_name, encoding="utf_8_sig", index=None)
    for i in range(1, len(file_list)):
        df = pd.read_csv(path + '\\' + file_list[i])
        df.to_csv(path + '\\' + save_file_name, encoding="utf_8_sig", index=None, header=False, mode='a+')
    print("将所有文件全部合成为一个文件，已完成")

###-------------下面这个是删除某一列的程序-----------------------###
def DeleteOneColumn(path):
    for files in glob.glob(path + '/*.csv'):
        df = pd.read_csv(files)
        df = df.drop(['idx'],axis=1)
        df.to_csv(files,index=None)


if __name__ == '__main__':
    # AddIdx(Folder_Path)  # 增加一列
    ManyToOneFile(Folder_Path)  #合成为一个文件
    # DeleteOneColumn(Folder_Path)  #删除某列数据







    # # 读取第一个CSV文件并包含表头
    # df = pd.read_csv(Folder_Path + '\\' + file_list[0])  # 编码默认UTF-8，若乱码自行更改

    # # 将读取的第一个CSV文件写入合并后的文件保存
    # df.to_csv(SaveFile_Path + '\\' + SaveFile_Name, encoding="utf_8_sig", index=True)
    #
    # # 循环遍历列表中各个CSV文件名，并追加到合并后的文件
    # for i in range(1, len(file_list)):
    #     df = pd.read_csv(Folder_Path + '\\' + file_list[i])
    #     df.to_csv(SaveFile_Path + '\\' + SaveFile_Name, encoding="utf_8_sig", index=True, header=False, mode='a+')
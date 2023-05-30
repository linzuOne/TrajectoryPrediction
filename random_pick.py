##从文件中随机选取训练的数据
import os
import random
import shutil

def moveFile(fileDir):
    fatherDir = os.path.dirname(fileDir)

    path1 = os.path.join(fatherDir, 'data')
    folder = os.path.exists(path1)
    if not folder:
        os.makedirs(path1)
    else:
        pass

    path2 = os.path.join(path1, 'train')
    folder = os.path.exists(path2)
    if not folder:
        os.makedirs(path2)
    else:
        pass

    path3 = os.path.join(path1, 'test')
    folder = os.path.exists(path3)
    if not folder:
        os.makedirs(path3)
    else:
        pass

    pathDir = os.listdir(fileDir)  # 取图片的原始路径
    filenumber = len(pathDir)
    # rate1 = 0.8  # 自定义抽取csv文件的比例
    rate1 = 0.8
    picknumber1 = int(filenumber * rate1)  # 按照rate比例从文件夹中取一定数量的文件
    sample1 = random.sample(pathDir, picknumber1)  # 随机选取picknumber数量的样本

    ##获取训练的船舶
    for train_name in sample1:
        shutil.copy(fileDir + '\\' + train_name, path2 + "\\" + train_name)

    ##获取测试的船舶
    sample2 = [test_names for test_names in pathDir if not test_names in sample1]
    for test_name in sample2:
        shutil.copy(fileDir + '\\' + test_name, path3 + "\\" + test_name)

    return path2,path3


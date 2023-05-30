#对相同mmsi号的csv进行合并
import glob
import csv
import shutil
import pandas
import os

#path = 'E:\\shuju\\2017\\解压后\\01\\1月份拆分之后\\new'
#path1 = 'E:\\shuju\\2017\\解压后\\01\\1月份拆分之后\\new2'
#合并之后的result.csv文件不能放在同一个文件夹下面，否则出错
# csv_list = glob.glob(path + '/*.csv') #查看同文件夹下的csv文件数
# print(u'共发现%s个CSV文件'% len(csv_list))

#===================================================================这个程序应该没有问题==============================================
def Merge(path):
    fatherDir = os.path.dirname(path)
    path1 = os.path.join(fatherDir,'AfterMerge')
    folder = os.path.exists(path1)
    if not folder:
        os.makedirs(path1)
    else:
        pass
    
    file_list = os.listdir(path)
    #print(file_list)
    file_list.sort(key=lambda x:int(x[:9]))
    #print(file_list)
    fileNum = len(file_list)
    
    j = 1
    count = 0
    
    while j < fileNum + 1:
        file_list = os.listdir(path)
        if file_list == []:
            print("全部合并成功")
            break
    
        for file in file_list: #循环读取同文件夹下的csv文件
            basename = os.path.splitext(file)[0]
            jiequ = basename[0:9]
            jiequqiansan = jiequ[0:3]
            jiequqianliu = jiequ[0:6]
            int_jiequ = int(jiequ)
            #print("第一个for file")
            # file_list
            count += 1
    
    
            for file1 in file_list:
                basename1 = os.path.splitext(file1)[0]
                jiequ1 = basename1[0:9]
                jiequqiansan1 = jiequ1[0:3]
                jiequqianliu1 = jiequ1[0:6]
                int_jiequ1 = int(jiequ1)
                #print("第二个 for file1")
    
                if int_jiequ != int_jiequ1:
                    # flag = 1
                    break
    
                if jiequqiansan == jiequqiansan1:
                    if jiequqianliu == jiequqianliu1:
                        if jiequ == jiequ1:
                            #print(file1)
                            oldaddress = os.path.join(path,file1)
                            tempaddress = os.path.join(path,'result.csv')
                            saveaddress = os.path.join(path1,jiequ + '.csv')
                            fr = open(oldaddress, 'rb').read()
                            with open(tempaddress, 'ab') as f:  # 将结果保存为result.csv
                                f.write(fr)
    
                            # shutil.move(tempaddress,saveaddress)
                            os.remove(oldaddress)
                            j += 1
                            #print(j)
    
            shutil.move(tempaddress, saveaddress)
    
            break
    
    print("共有" + str(j-1) + "个文件")
    print("共合成" + str(count) + "个文件")
    return path1









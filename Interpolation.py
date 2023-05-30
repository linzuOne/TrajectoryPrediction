import csv
import time
import copy
import math
import glob
import os
import matplotlib.pyplot as plt
#===========================================================
#需要将列表里的数据全部转换成浮点数，所以如果存在 'IMO9340544' 这种的，程序会出错，所以需要先将这些列删除
# 其他多余的列可以放进去，只要能转换成浮点数就可以
#===========================================================
# 文件的输入格式： ['BaseDateTime','LAT', 'LON', 'SOG'，‘COG’, 'MMSI', 'idx']
## 上面的格式必须是一模一样，不然代码需要改动
# 读取csv文件
# path = 'E:\\shuju\\temp\\temp1'
def InterPolation(path):
    dim = 7   #文件输入的列数  ['BaseDateTime','LAT', 'LON', 'SOG'，‘COG’, 'MMSI', 'idx']  7列，所以 dim = 7

    ## ==================== 插值后的文件在 下面 目录 下 ==================
    after_Interpolation_path = os.path.join(path, "Interpolation")
    folder = os.path.exists(after_Interpolation_path)
    if not folder:
        os.makedirs(after_Interpolation_path)
    else:
        pass

    for files in glob.glob(path + '/*.csv'):
        with open(files, 'r') as f:
            reader = csv.reader(f)
            result = list(reader) # 将数据空间转换成嵌套列表
            L = len(result)
            for i in range(1,L): #len(result)包括了表头， result[L-1]是最后一个数
                start_time = result[i][0]
                s_t = time.strptime(start_time, "%Y-%m-%dT%H:%M:%S")
                # print(s_t)
                result[i][0] = float(time.mktime(s_t))  #将时间戳转为秒
            # 下面遍历列表（跳过表头），将列表里的数据转换成浮点数，便于后续处理
            for i in range(1, L):
                result[i] = list(map(float, result[i]))  #将列表里的数据全部转换成浮点数

            mmsi = result[1][5]  ## 读取了 第一行, 第 5列的 MMSI，从 0 开始
            idx = result[1][6]

        new_deepCopy_result = copy.deepcopy(result)   # 复制原列表

        section = math.ceil((result[len(result)-1][0] - result[1][0]) / 60)  #section表示按照60切分，共section个时间点
        segment = section - L + 1   #需要给 new_deepCopy_result 增加segment个 列表

        for i in range(L,section+1):   #共 section - L + 1 个 i
            new_deepCopy_result.append([])
            for j in range(dim):
                new_deepCopy_result[i].append([])    # 给 new_deepCopy_result 延长列表的长度

    #========================= 开始插值====================================
        k = 1
        j_record = 2
        count = 0

        while(1):
            count += 1
            if count == section:          # 操作 section 次
                break
            for i in range(k,section+1):
                next_time = new_deepCopy_result[i][0] + 60  # 加上60秒
                for j in range(j_record,L):
                    if result[j][0] == next_time:
                        new_deepCopy_result[i + 1][0] = next_time   #时间
                        new_deepCopy_result[i + 1][1] = result[j][1]   #纬度
                        new_deepCopy_result[i + 1][2] = result[j][2]   #经度
                        new_deepCopy_result[i + 1][3] = result[j][3]   #速度
                        new_deepCopy_result[i + 1][4] = result[j][4]   #角度
                        new_deepCopy_result[i + 1][5] = mmsi
                        new_deepCopy_result[i + 1][6] = idx
                        k = i + 1
                        j_record = j + 1
                        break
                    else:
                        if result[j][0] > next_time and result[j-1][0] < next_time:
                            if j == j_record:
                                lat_new = (result[j][1] - new_deepCopy_result[i][1]) / (result[j][0] - new_deepCopy_result[i][0]) * (next_time - new_deepCopy_result[i][0]) + new_deepCopy_result[i][1]
                                lon_new = (result[j][2] - new_deepCopy_result[i][2]) / (result[j][0] - new_deepCopy_result[i][0]) * (next_time - new_deepCopy_result[i][0]) + new_deepCopy_result[i][2]
                                sog_new = (result[j][3] - new_deepCopy_result[i][3]) / (result[j][0] - new_deepCopy_result[i][0]) * (next_time - new_deepCopy_result[i][0]) + new_deepCopy_result[i][3]
                                cog_new = (result[j][4] - new_deepCopy_result[i][4]) / (result[j][0] - new_deepCopy_result[i][0]) * (next_time - new_deepCopy_result[i][0]) + new_deepCopy_result[i][4]

                                new_deepCopy_result[i+1][0] = next_time
                                new_deepCopy_result[i+1][1] = lat_new  # 先对经纬度插值
                                new_deepCopy_result[i+1][2] = lon_new
                                new_deepCopy_result[i+1][3] = sog_new
                                new_deepCopy_result[i+1][4] = cog_new
                                new_deepCopy_result[i + 1][5] = mmsi
                                new_deepCopy_result[i + 1][6] = idx
                            else:
                                lat_new = (result[j][1] - result[j-1][1]) / (result[j][0] - result[j-1][0]) * (next_time - result[j-1][0]) + result[j-1][1]
                                lon_new = (result[j][2] - result[j-1][2]) / (result[j][0] - result[j-1][0]) * (next_time - result[j-1][0]) + result[j-1][2]
                                sog_new = (result[j][3] - result[j-1][3]) / (result[j][0] - result[j-1][0]) * (next_time - result[j-1][0]) + result[j-1][3]
                                cog_new = (result[j][4] - result[j-1][4]) / (result[j][0] - result[j-1][0]) * (next_time - result[j-1][0]) + result[j-1][4]

                                new_deepCopy_result[i+1][0] = next_time
                                new_deepCopy_result[i+1][1] = lat_new     #先对经纬度插值
                                new_deepCopy_result[i+1][2] = lon_new
                                new_deepCopy_result[i+1][3] = sog_new
                                new_deepCopy_result[i+1][4] = cog_new
                                new_deepCopy_result[i + 1][5] = mmsi
                                new_deepCopy_result[i + 1][6] = idx
                            k = i + 1
                            j_record = j
                            break
                break
    # ================================= 开始插值==============================================
    # ================================将秒数转换为时间戳=====================================
        for i in range(1,section+1):      #将秒数转换为时间戳
            local_time = time.localtime(new_deepCopy_result[i][0])
            new_deepCopy_result[i][0] = time.strftime("%Y-%m-%dT%H:%M:%S",local_time)
    # ================================以上将秒数转换为时间戳=====================================
        ## ==================== 插值后的文件存放在下面 ==================

        file_name = os.path.basename(files)
        save_file_name = after_Interpolation_path + '\\' + file_name
        file_name_without = os.path.basename(files).split('.')[0]
    #===================上面是插值后的文件存放路径===============================
        # picture_Save = os.path.join(os.path.dirname(files), 'save_Picture')  # 存储图片
        # folder = os.path.exists(picture_Save)
        # if not folder:
        #     os.makedirs(picture_Save)
        # else:
        #     pass
    #==========================上面是图片的存放路径================================
        with open(save_file_name, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            # 由于我转换数据类型及插值的时候跳过了表头，故不需要再写入表头
            # 不需要写 writer.writerow(["BaseDateTime", "LAT", "LON",'SOG'])   # 先写入columns_name
            writer.writerows(new_deepCopy_result)   #写入多行用writerows
            print("ok")

    #=======================画图==================================
        # result_lat,result_lon = [],[]
        # for result_i in range(1,L):
        #     result_lat.append(result[result_i][1])
        #     result_lon.append(result[result_i][2])
        #
        # new_lat,new_lon = [],[]
        # for new_i in range(1,section+1):
        #     new_lat.append(new_deepCopy_result[new_i][1])
        #     new_lon.append(new_deepCopy_result[new_i][2])
        #
        # plt.plot(result_lon,result_lat,marker='o')
        # plt.plot(new_lon,new_lat,marker='x')
        # # plt.show()
        # plt.savefig(picture_Save + '\\' + file_name_without + '.jpg')
        # plt.clf()
        # plt.cla()
        # plt.close()

    return after_Interpolation_path
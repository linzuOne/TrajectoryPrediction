#清除速度异常值
#清除角度异常值
#清除离群点
#异常时间需要去除吗
#这里只清除单个离群点，多个离群点不考虑
import pandas as pd
import glob
import time
from math import sin, asin, cos, radians, fabs, sqrt
import matplotlib
import matplotlib.pyplot as plt
import os

EARTH_RADIUS = 6371000  #地球半径6371千米

# 计算两个经纬度之间的直线距离
def hav(theta):
    s = sin(theta / 2)
    return s * s

def get_distance_hav(lat0, lng0, lat1, lng1):
    # "用haversine公式计算球面两点间的距离。"
    # 经纬度转换成弧度
    lat0 = radians(lat0)
    lat1 = radians(lat1)
    lng0 = radians(lng0)
    lng1 = radians(lng1)

    dlng = fabs(lng0 - lng1)
    dlat = fabs(lat0 - lat1)
    h = hav(dlat) + cos(lat0) * cos(lat1) * hav(dlng)
    distance = 2 * EARTH_RADIUS * asin(sqrt(h))
    return distance

#先写清除离群点
def deleteErrorPoint(path):
    for file in glob.glob(path + '/*.csv'):
        df = pd.read_csv(file)
        j = 2
        remove_row_list = []
        for i in range(j,len(df)):  # i=0 是第一行数据  # len 最大260，df['SOG'][259]最多到259
            #计算两个轨迹点之间的距离
            distance1 = get_distance_hav(df['LAT'][i-2], df['LON'][i-2], df['LAT'][i-1], df['LON'][i-1]) #第 1 个点 和 第 2 个点
            distance2 = get_distance_hav(df['LAT'][i-1], df['LON'][i-1], df['LAT'][i], df['LON'][i]) #第 2 个点 和 第 3 个点
            distance3 = get_distance_hav(df['LAT'][i-2], df['LON'][i-2], df['LAT'][i], df['LON'][i]) # 第 1 个点 和 第 3 个点

            #获取两个轨迹点之间的时间差，以秒为单位
            first_time = df['BaseDateTime'][i-2]
            first_time = time.strptime(first_time, "%Y-%m-%dT%H:%M:%S")
            first_time = float(time.mktime(first_time))  # 将时间戳转为秒

            second_time = df['BaseDateTime'][i-1]
            second_time = time.strptime(second_time, "%Y-%m-%dT%H:%M:%S")
            second_time = float(time.mktime(second_time))  # 将时间戳转为秒

            last_time = df['BaseDateTime'][i]
            last_time = time.strptime(last_time, "%Y-%m-%dT%H:%M:%S")
            last_time = float(time.mktime(last_time))  # 将时间戳转为秒

            gap1 = second_time - first_time  #第 2 个点与 第 1 个点的差
            gap2 = last_time - second_time   #第 3 个点与 第 2 个点的差
            gap3 = last_time - first_time #第 3 个点 和 第 1 个点 的差

            #获取前面一个时刻的速度
            #这里的前提条件是 速度 正常，所以在清除离群点之前需要消除速度异常点，将异常速度改成正常值
            sog1 = df['SOG'][i-2]  #单位是 节
            sog1 = sog1 * 0.5144444  #一节等于  0.5144444米/秒  转换为米/秒

            sog2 = df['SOG'][i-1]
            sog2 = sog2 * 0.5144444

            # #速度乘上时间
            # df = df.drop(df.index[[i+1]])
            if i == 2:
                if sog1 * gap1 < 0.8 * distance1:
                    if sog1 * (gap1 + gap2) < 0.7 * distance3:
                        remove_row_list.append(i-2)
            if sog1 * gap1 < 0.8 * distance1 and sog2 * gap2 < 0.8 * distance2 :  #如果时间乘上前一时刻的速度大于1.2倍的距离，则删除掉
                remove_row_list.append(i-1)
            if i == len(df) - 1:
                if sog1 * gap3 < 0.7 * distance3:
                    remove_row_list.append(i)

        df = df.drop(df.index[remove_row_list])
        df.to_csv(file,index=None)
        print(file + "完成了")




import matplotlib
import matplotlib.pyplot as plt
import glob
import os
import pandas as pd

def Picture(path):
    matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
    plt.rcParams['axes.unicode_minus']=False
    x_data = []
    y_data = []

    path1 = os.path.join(path,"picture")
    folder = os.path.exists(path1)
    if not folder:
        os.makedirs(path1)
    else:
        pass

    for files in glob.glob(path + '/*.csv'):
        data = pd.read_csv(files,sep=',').iloc[:,2:4].values    ## 注意： 这里 iloc[:,2:4].values表示纬度在第二列，经度在第三列，第四列取不到，从第零列开始算，如果纬度和经度不在第二列和第三列，这里需要改一下
        x_data = data[:,1]     # LON经度
        y_data = data[:,0]     # LAT纬度

        front = os.path.basename(files)
        jiequ = os.path.splitext(front)[0]
        # plt.plot(x_data, y_data)
        plt.plot(x_data, y_data, 'bx-')
        x_data = []
        y_data = []

        plt.title(jiequ)
        # plt.legend()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.savefig(path1 + '\\' + jiequ + '.jpg')
        # plt.show()
        plt.clf()
        plt.close()


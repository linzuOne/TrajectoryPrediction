#长度小于5，宽度小于4的删除
#这个程序太冗余，创建了好几个文件夹
import pandas as pd
import glob
import os
import shutil
import math

def delete_smallship(path):
    # smallship = os.path.join(path,"小型船舶")
    # folder = os.path.exists(smallship)
    # if not folder:
    #     os.makedirs(smallship)
    # else:
    #     pass
    
    largeship = os.path.join(path,"大型船舶")
    folder1 = os.path.exists(largeship)
    if not folder1:
        os.makedirs(largeship)
    else:
        pass
    
    # NoneButLarge = os.path.join(path,"空但是不是小船")
    # folder2 = os.path.exists(NoneButLarge)
    # if not folder2:
    #     os.makedirs(NoneButLarge)
    # else:
    #     pass
    
    # BothNone = os.path.join(path,"长宽都是空")
    # folder3 = os.path.exists(BothNone)
    # if not folder3:
    #     os.makedirs(BothNone)
    # else:
    #     pass
    
    for files in glob.glob(path + '/*.csv'):
        df = pd.read_csv(files)
        basename = os.path.basename(files)
    
        # length = len(open(files).readlines())  获取行数
        ##==========================================================================
        # if math.isnan(df['Length'][0]) and math.isnan(df['Width'][0]):
        #     shutil.move(files,os.path.join(BothNone,basename))
        #
        #
        # elif math.isnan(df['Length'][0]) or math.isnan(df['Width'][0]):
        #     if df['Length'][0] < 5 or df['Width'][0] < 4:
        #         shutil.move(files,os.path.join(smallship,basename))
        #
        #     else:
        #         shutil.move(files,os.path.join(NoneButLarge,basename))
        ##===========================================================================
        ## 将尺寸不符合要求的船删除掉，上面是移走

        if math.isnan(df['Length'][0]) or math.isnan(df['Width'][0]):
            os.remove(files)

        else:
            if df['Length'][0] < 5 or df['Width'][0] < 4:
                # shutil.move(files, os.path.join(smallship, basename))
                os.remove(files)

            else:
                shutil.move(files,os.path.join(largeship,basename))
        #print(files + "已经完成")
    print("删除小尺寸船舶，成功")
    return largeship

 
# 交换列的顺序

import pandas as pd
file = 'E:\\shuju\\sample_train.csv'

df=pd.read_csv(file)
df=df.iloc[:,[3,4,0,1,2,5,6,7,8,9,10,11]]
df.to_csv(file,header=None,index=None)   #这里注意：去除表头，如果不去除表头，则不写 header=None
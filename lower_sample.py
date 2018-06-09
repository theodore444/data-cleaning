#-*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# 解决中文显示问题
mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False
#随机种子
np.random.seed(14)

#下采样函数
def lower_sampling(big_data,sample_number):
    if sample_number >= len(big_data):
        return big_data
    #设置采样索引
    row_index = set()
    while (len(row_index) != sample_number):
        index = np.random.randint(0,len(big_data),1)[0]
        row_index.add(index)
    #转换为df
    sample_df = df.iloc[list(row_index)]
    print(sample_df)
    #获取剩下的bigsample
    other_row_index = [i for i in range(len(big_data)) if i not in row_index]
    after_sampled_df = df.iloc[other_row_index]
    return sample_df,after_sampled_df



#生成数据
# EasyEnsemble方式
if __name__ == '__main__':
    #生成正例
    category1 = np.random.randint(0,10,[10000,5]).astype(np.float)
    label1 = np.array([1] * 10000).reshape(-1,1)
    data1 = np.concatenate((category1,label1),axis=1)
    #生成反例
    category2 = np.random.randint(8, 18, [10, 5]).astype(np.float)
    label2 = np.array([0] * 10).reshape(-1, 1)
    data2 = np.concatenate((category2, label2), axis=1)
    #融合正反例
    name = ['A','B','C','D','E','label']
    data = np.concatenate((data1,data2),axis=0)
    df = pd.DataFrame(data,columns=name)

    smalldata = df[df.label != 1]
    bigdata = df[df.label == 1]
    samplenumber = 200
    (sample_data,bigdata) = lower_sampling(bigdata,samplenumber)

    final_df = pd.concat([smalldata,sample_data],ignore_index = True)
    print(final_df)


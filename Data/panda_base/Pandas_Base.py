# _*_ coding : utf-8 _*_
# @TIme : 2024/7/31 21:38
# @Author : zhangweilaing
# @file ： Pandas_Base
import pandas as pd
#数据读取
        # df_csv = pd.read_csv('Data/my_csv.csv')
        # print(df_csv)
        # 常用公共参数
            # header=None 表示第一行不作为列名
            # print(pd.read_csv('Data/my_csv.csv',header= None))
            # index_col 表示把某一列或几列作为索引
            #print(pd.read_csv('Data/my_csv.csv',index_col=['col1','col2']))
            #usecols 表示读取列的集合，默认读取所有的列
            #print(pd.read_csv('Data/my_csv.csv',usecols=['col1','col2']))
            # parse_dates 表示需要转化为时间的列
            #print(pd.read_csv('Data/my_csv.csv',parse_dates=['col5']))
            # nrows 表示读取的数据行数
            #print(pd.read_csv('Data/my_csv.csv',nrows=2))


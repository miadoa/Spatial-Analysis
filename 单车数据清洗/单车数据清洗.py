# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 19:38:42 2018

@author: 66457
"""
#检查重复项是否被正确识别（可删）
#duplicate=df.duplicated(['time','bike_id'])


import pandas as pd
import numpy as np
from pandas import DataFrame
import os
import time

#获取文件名列表
files=os.listdir()
#存放筛选过的文件名
data=[]
#存放所有dataframe
frame=[]
#筛选csv文件结尾的文件
for file in files:
    if os.path.splitext(file)[1]=='.csv':
        data.append(file)

#开始时间        
start_time0=time.time()
#文件计数
count=0
num=0
for file_path in data:
    #开始时间
    start_time=time.time()
    count+=1
    print("开始读取第%d个文件%s" %(count,file_path))
    df=pd.read_csv(file_path)
    #修改列名，存在问题
    num_df=len(df)
    num+=num_df
    df.columns=['time','b','a','bike_id','c','d','longitude','latitude']
    #删除不用的列
    df=df.drop(['a','b','c','d'],axis=1)
    #time替换字符串T
    df['time']=df['time'].str.replace('T',' ')
    frame.append(df)
    
    #结束时间
    end_time=time.time()
    last=end_time-start_time
    print("该文件读取完毕，耗时%.2f秒" %last)
    print("该文件长度为%d" %num_df)

end_time=time.time()
last=end_time-start_time0
print("所有文件读取完毕，耗时%.2f秒" %last)
print("所有文件长度为%d" %num)

start_time2=time.time()
df_all=pd.concat(frame)
#每个采集时刻：一个单车只曝光一次
df_all=df_all.drop_duplicates(['time','bike_id'])
#所有采集时刻：单车必须移动过
df_all=df_all.drop_duplicates(['bike_id','longitude'])
#单车的曝光次数不止一次,True是前面有过的项，False是前面没有的
#print(df_all.duplicated(['bike_id']))
df_all=df_all[df_all.duplicated(['bike_id'])]
df_all=df_all.reset_index(drop=True)

#数据清洗时间计算
end_time2=time.time()
last2=end_time2-start_time2
print("所有文件清洗完毕，耗时%.2f秒" %last2)

start_time3=time.time()
#df_all.to_csv("D:/myAdmin/OneDrive - i.b.school.nz/Homework/1.15空间规划新技术/mobike_data/test.csv", encoding = 'utf-8',index=False)
end_time3=time.time()
last3=end_time3-start_time3
print("文件导出完毕，耗时%.2f秒" %last3)
print("清洗之后的数据为%d" % len(df_all))

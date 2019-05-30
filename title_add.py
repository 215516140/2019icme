# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 10:29:02 2019

@author: Administrator
"""
import tensorflow as tf
import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
import re
from sklearn.cluster import KMeans

#data = pd.read_csv('title.csv')

data = pd.read_csv('./input/final_track2_train.txt', sep='\t', names=[
   'uid', 'user_city', 'item_id', 'author_id', 'item_city', 'channel', 'finish', 'like', 'music_id', 'did', 'creat_time', 'video_duration'])
data=data.drop(data[(data.item_city==-1)&(data.user_city==-1)].index)


'''
data.drop(['Unnamed: 0'],axis=1,inplace=True)
data1 = pd.read_csv('title_kmeans.csv')
data1.drop(['Unnamed: 0'],axis=1,inplace=True)

data_title=pd.concat([data['0'],data1],axis=1,ignore_index=False)

data_title=data_title.to_csv("title.csv")


num_clusters = 20
km_cluster = KMeans(n_clusters=num_clusters, max_iter=300, n_init=40, \
                    init='k-means++',n_jobs=-1)
result = km_cluster.fit_predict(title)
title=DataFrame(result)
title.to_csv("title_kmeans.csv")


pattern1 = r'^5301'
str_data=data['creat_time'].apply(str)
data['creat_time'][str_data.str.contains(pattern1)]=1

pattern2 = r'^5302'

data['creat_time'][str_data.str.contains(pattern2)]=2

pattern3 = r'^5303'

data['creat_time'][str_data.str.contains(pattern3)]=3

pattern4 = r'^5304'

data['creat_time'][str_data.str.contains(pattern4)]=4

pattern5 = r'^5305'

data['creat_time'][str_data.str.contains(pattern5)]=5

pattern6 = r'^5306'

data['creat_time'][str_data.str.contains(pattern6)]=6

pattern7 = r'^5307'

data['creat_time'][str_data.str.contains(pattern7)]=7

pattern8 = r'^5308'

data['creat_time'][str_data.str.contains(pattern8)]=8
'''
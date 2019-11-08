# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:38:46 2019

@author: Ivan
"""
import pandas as pd


def cut_dataframe(df, cut = 6, cutColumn = '你想切割的欄位'):
    label = []
    tolerance = (df[cutColumn].max()-df[cutColumn].min())/cut #先計算切割的公差
    for i in range( cut-1): #開始創造切割label，最後一個值不要跑出來，因為要是最大值，用加的怕會有小數點誤差
        label.append(str(int(df[cutColumn].min()+tolerance*i)) + ' - ' + str(int(df[cutColumn].min()+tolerance*(i+1))))
    # 加上最後一位
    label.append(str(int(df[cutColumn].min()+tolerance*(i+1))) + ' - ' + str(int(df[cutColumn].max())))
    
    return pd.cut(df[cutColumn] , cut, labels=label), label #切割後的分類內容

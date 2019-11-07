# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 12:41:13 2019

@author: Ivan
"""
import pandas as pd
import random

def make_data():
    dicA = {
            '品牌':['A' for x in range(100)],
            '顏色':['#B9313B' for x in range(100)],
            '價格':[x*10+random.randint(-9,9) for x in range(100)],
            '價值':[x*5+random.randint(-9,9) for x in range(100)],
            '市佔率':[x*3+random.randint(-3,7) for x in range(100)],
            '年分':[1920+x for x in range(100)]
            }
    dfA = pd.DataFrame(dicA)
    
    dicB = {
            '品牌':['B' for x in range(100)],
            '顏色':['#279b37' for x in range(100)],
            '價格':[x*10+random.randint(-9,9) for x in range(100)],
            '價值':[x*5+random.randint(-5,9) for x in range(100)],
            '市佔率':[15+random.randint(-3,7) for x in range(100)],
            '年分':[1920+x for x in range(100)]
            }
    dfB = pd.DataFrame(dicB) 
    
    dicC = {
            '品牌':['C' for x in range(100)],
            '顏色':['#FCFF90' for x in range(100)],
            '價格':[x*10+random.randint(-9,9) for x in range(100)],
            '價值':[300+random.randint(-5,9) for x in range(100)],
            '市佔率':[x*2+random.randint(-3,7) for x in range(100)],
            '年分':[1920+x for x in range(100)]
            }
    dfC = pd.DataFrame(dicC) 
    
    dicD = {
            '品牌':['D' for x in range(100)],
            '顏色':['#02FCF3' for x in range(100)],
            '價格':[700+random.randint(-9,30) for x in range(100)],
            '價值':[x*2+random.randint(-5,9) for x in range(100)],
            '市佔率':[x*2+random.randint(-3,7) for x in range(100)],
            '年分':[1920+x for x in range(100)]
            }
    dfD = pd.DataFrame(dicD) 
    
    dicE = {
            '品牌':['E' for x in range(100)],
            '顏色':['#EEA938' for x in range(100)],
            '價格':[200+x*10+random.randint(-9,9) for x in range(100)],
            '價值':[300+x*5+random.randint(-9,9) for x in range(100)],
            '市佔率':[x*3+random.randint(-3,7) for x in range(100)],
            '年分':[1920+x for x in range(100)]
            }
    dfE = pd.DataFrame(dicE) 

    dicF = {
            '品牌':['F' for x in range(100)],
            '顏色':['#FF5A18' for x in range(100)],
            '價格':[200+x*10+random.randint(-9,9) for x in range(100)],
            '價值':[700++random.randint(-9,9) for x in range(100)],
            '市佔率':[30+x*3+random.randint(-3,7) for x in range(100)],
            '年分':[1920+x for x in range(100)]
            }
    dfF = pd.DataFrame(dicF)
    
    dicG = {
            '品牌':['G' for x in range(100)],
            '顏色':['#005118' for x in range(100)],
            '價格':[1000+random.randint(-9,9) for x in range(100)],
            '價值':[700+random.randint(-9,9) for x in range(100)],
            '市佔率':[330-x*3+random.randint(-3,7) for x in range(100)],
            '年分':[1920+x for x in range(100)]
            }
    dfG = pd.DataFrame(dicG)
    
    dicH = {
            '品牌':['H' for x in range(100)],
            '顏色':['#DDDDDD' for x in range(100)],
            '價格':[1000+x**0.5+random.randint(-9,9) for x in range(100)],
            '價值':[600+x**0.5+random.randint(-9,9) for x in range(100)],
            '市佔率':[130+x**0.5+random.randint(-3,7) for x in range(100)],
            '年分':[1920+x for x in range(100)]
            }
    dfH = pd.DataFrame(dicH)
    return pd.concat([dfA,dfB,dfC,dfD,dfE,dfF,dfG,dfH],axis=0)  

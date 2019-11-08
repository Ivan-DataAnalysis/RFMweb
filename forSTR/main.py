# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:16:36 2019

@author: Ivan
"""
from os.path import dirname, join
import pandas as pd
from bokeh.io import curdoc
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource, Select, Span
from bokeh.plotting import figure
#自訂涵式庫
import cut_dataframe
# 設定資料
insurance = pd.read_csv(join(dirname(__file__), "insurance.csv"), encoding='utf-8')
cut=4

Spectral11 = ['#B9313B','#279b37','#FCFF90','#02FCF3','#EEA938','#FF5A18','#005118',
'#DDDDDD', '#AAAAAA', '#888888', '#666666', '#444444', '#000000', '#4B0082',
'#FFB7DD', '#FF88C2', '#FF44AA', '#FF0088', '#C10066', '#A20055', '#8C0044',
'#FFCCCC', '#FF8888', '#FF3333', '#FF0000', '#CC0000', '#AA0000', '#880000',
'#FFC8B4', '#FFA488', '#FF7744', '#FF5511', '#E63F00', '#C63300', '#A42D00',
'#FFDDAA', '#FFBB66', '#FFAA33', '#FF8800', '#EE7700', '#CC6600', '#BB5500',
'#FFEE99', '#FFDD55', '#FFCC22', '#FFBB00', '#DDAA00', '#AA7700', '#886600',
'#FFFFBB', '#FFFF77', '#FFFF33', '#FFFF00', '#EEEE00', '#BBBB00', '#888800',
'#EEFFBB', '#DDFF77', '#CCFF33', '#BBFF00', '#99DD00', '#88AA00', '#668800',
'#CCFF99', '#BBFF66', '#99FF33', '#77FF00', '#66DD00', '#55AA00', '#227700',
'#99FF99', '#66FF66', '#33FF33', '#00FF00', '#00DD00', '#00AA00', '#008800',
'#BBFFEE', '#77FFCC', '#33FFAA', '#00FF99', '#00DD77', '#00AA55', '#008844',
'#AAFFEE', '#77FFEE', '#33FFDD', '#00FFCC', '#00DDAA', '#00AA88', '#008866',
'#99FFFF', '#66FFFF', '#33FFFF', '#00FFFF', '#00DDDD', '#00AAAA', '#008888',
'#CCEEFF', '#77DDFF', '#33CCFF', '#00BBFF', '#009FCC', '#0088A8', '#007799',
'#CCDDFF', '#99BBFF', '#5599FF', '#0066FF', '#0044BB', '#003C9D', '#003377',
'#CCCCFF', '#9999FF', '#5555FF', '#0000FF', '#0000CC', '#0000AA', '#000088',
'#CCBBFF', '#9F88FF', '#7744FF', '#5500FF', '#4400CC', '#2200AA', '#220088',
'#D1BBFF', '#B088FF', '#9955FF', '#7700FF', '#5500DD', '#4400B3', '#3A0088',
'#E8CCFF', '#D28EFF', '#B94FFF', '#9900FF', '#7700BB', '#66009D', '#550088',
'#F0BBFF', '#E38EFF', '#E93EFF', '#CC00FF', '#A500CC', '#7A0099', '#660077',
'#FFB3FF', '#FF77FF', '#FF3EFF', '#FF00FF', '#CC00CC', '#990099', '#770077']

columns = sorted(insurance.columns)
thestr = [x for x in columns if insurance[x].dtype == object]
        

#下拉式選單設定
x_axis = Select(value=thestr[0], title='X欄位', options=thestr)


#下拉式選單，觸發圖片重畫
def update_plot():
    # 先進行欄位切割
    insurance['BMI範圍'], X_label = cut_dataframe.cut_dataframe(insurance, cut = cut, cutColumn = 'BMI')
    insurance['年齡範圍'], Y_label = cut_dataframe.cut_dataframe(insurance, cut = cut, cutColumn = '年齡')


    fruits = insurance[x_axis.value].value_counts().index.tolist() # 準備X刻度
    count=0
    theplot=[] #準備放每個小圖的畫布
    thesource=[] #準備放每個小圖的資料
    thecolumn = []
    for i in Y_label[::-1]: # 由於axes畫布排列的關係，頻率必須要反著放
        therow = []
        for j in X_label: # 近因
            
            if insurance[(insurance['年齡範圍']==i) & (insurance['BMI範圍']==j)].shape[0] != 0: # 檢查這個方格有沒有數據
                s_data = insurance[(insurance['年齡範圍']==i) & (insurance['BMI範圍']==j)]
                counts = s_data.groupby(x_axis.value,as_index = False )['毛利'].sum()['毛利'].tolist()
            else:
                counts = [] #沒有數值的畫就顯示空的
                
            theplot.append(figure(plot_height=400, plot_width=400, title='年齡範圍'+i + "   " + 'BMI範圍'+j,
                  tools="crosshair,pan,reset,save,wheel_zoom",
                  tooltips=[("Title", "@y")],
                  x_range=fruits,
                  y_range=(0, 1000000)))
                
            # 繪圖設定 
            thesource.append(ColumnDataSource(data=dict(x=fruits, y=counts, color=Spectral11[:len(fruits)])))
            # 畫棒狀圖
            theplot[count].vbar(x='x', top='y', width=0.9, color='color', legend="x" , source=thesource[count])
            theplot[count].xaxis.axis_label = x_axis.value #修改X標籤
            theplot[count].yaxis.axis_label = x_axis.value + '總數量'  #修改Y標籤
            theplot[count].xgrid.grid_line_color = None # 去掉垂直線
            theplot[count].legend.orientation = "horizontal" # 圖例水平展示
            theplot[count].legend.location = "top_center" #圖例置中
            # 四個區塊分顏色
            if len(therow) > cut/2-1 and len(thecolumn) > cut/2-1:
                theplot[count].background_fill_color = "#ffcdd2" #紅色
            elif len(therow) > cut/2-1 and len(thecolumn) < cut/2:
                theplot[count].background_fill_color = "#FFF9C4" #黃色
            elif len(therow) < cut/2 and len(thecolumn) > cut/2-1:
                theplot[count].background_fill_color = "#BBDEFB" #藍色
            else:
                theplot[count].background_fill_color = "#B2DFDB" #綠色
            hline = Span(location=int(s_data.groupby(x_axis.value,as_index = False )['毛利'].sum()['毛利'].mean()), dimension='width', line_color='red', line_width=3)
    
            theplot[count].renderers.extend([hline])
            therow.append(theplot[count])
            count= count+1
        thecolumn.append(row(therow))
    return column(thecolumn)
        


#檢查當有任何選單、拉鍊被觸動時，觸發變動
def update(attr, old, new):
    layout.children[1] = update_plot()
    
for w in [x_axis]:
    w.on_change('value', update)


# 畫布與選單編排
layout = row(column(x_axis),column(update_plot()), width=2000)
curdoc().add_root(layout)
curdoc().title = "RFM_STR" 
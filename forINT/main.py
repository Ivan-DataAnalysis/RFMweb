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
from bokeh.models.widgets import DataTable, TableColumn, NumberFormatter
from bokeh.plotting import figure
#自訂涵式庫
import cut_dataframe
# 設定資料
insurance = pd.read_csv(join(dirname(__file__), "insurance.csv"), encoding='utf-8')
cut=4

columns = sorted(insurance.columns)
theint = [x for x in columns if insurance[x].dtype == 'int64' or insurance[x].dtype == 'float64']


#下拉式選單設定
x_axis = Select(value=theint[3], title='X欄位', options=theint)
y_axis = Select(value=theint[5], title='Y欄位', options=theint)


#定義最大刻度，讓刻度標準化
def findBigerValue(col):
    return insurance[col].max()

#定義最小刻度，讓刻度標準化
def findSmallerValue(col):
    return insurance[col].min()


#下拉式選單，觸發圖片重畫
def update_plot():
    theplot=[] #準備放每個小圖的畫布
    thesource=[] #準備放每個小圖的資料（畫布用的資料）
    # 先進行欄位切割
    insurance['BMI範圍'], X_label = cut_dataframe.cut_dataframe(insurance, cut = cut, cutColumn = 'BMI')
    insurance['年齡範圍'], Y_label = cut_dataframe.cut_dataframe(insurance, cut = cut, cutColumn = '年齡')

    thecolumn = []
    count=0 #準備這個數值，等等每個小圖進去畫
    for i in Y_label[::-1]: # 由於axes畫布排列的關係，頻率必須要反著放
        therow = []
        for j in X_label: # 近因


            if insurance[(insurance['年齡範圍']==i) & (insurance['BMI範圍']==j)].shape[0] != 0: # 檢查這個方格有沒有數據
                s_data = insurance[(insurance['年齡範圍']==i) & (insurance['BMI範圍']==j)]

            else:
                s_data = pd.DataFrame({x_axis.value:[], y_axis.value:[]}) #沒有數值的畫就顯示空的 
                
            sz = [9 for xx in range(len(s_data[x_axis.value]))]
            c = ['#31AADE' for xx in range(len(s_data[x_axis.value]))]
            thesource.append(ColumnDataSource(data=dict(x=s_data[x_axis.value].values, 
                                                        y=s_data[y_axis.value].values,
                                                        sz=sz,
                                                        c = c,
                                                        s_data = s_data
                                                        )))

            theplot.append(figure(plot_height=400, 
                                  plot_width=400, 
                                  title='BMI範圍' + i + "   " + '年齡範圍' + j,
                                  tools="crosshair,pan,reset,save,wheel_zoom",
                                  sizing_mode="scale_both",
                                  x_range=(findSmallerValue(x_axis.value), findBigerValue(x_axis.value)),
                                  y_range=(findSmallerValue(y_axis.value), findBigerValue(y_axis.value)), 
                                  tooltips = [
                                            (x_axis.value, "$x"),
                                            (y_axis.value, "$y")
                                            ]
                                  ))
     
            
            # 畫點陣圖
            theplot[count].circle(x='x', 
                                   y='y', 
                                   size='sz', 
                                   color='c', 
                                   line_color='white', 
                                   hover_alpha=0.5, 
                                   alpha=0.6,
                                   source=thesource[count])
            
            theplot[count].xaxis.axis_label = x_axis.value #修改X標籤
            theplot[count].yaxis.axis_label = y_axis.value #修改Y標籤
            theplot[count].xaxis.major_label_orientation = pd.np.pi / 4 #把X標籤斜角度30度
            hline = Span(location=int(s_data[y_axis.value].mean()), dimension='width', line_color='red',line_dash='dashed', line_width=1)
            vline = Span(location=int(s_data[x_axis.value].mean()), dimension='height', line_color='red',line_dash='dashed', line_width=1)
            theplot[count].renderers.extend([hline, vline])
            # 四個區塊分顏色
            if len(therow) > cut/2-1 and len(thecolumn) > cut/2-1:
                theplot[count].background_fill_color = "#ffcdd2" #紅色
            elif len(therow) > cut/2-1 and len(thecolumn) < cut/2:
                theplot[count].background_fill_color = "#FFF9C4" #黃色
            elif len(therow) < cut/2 and len(thecolumn) > cut/2-1:
                theplot[count].background_fill_color = "#BBDEFB" #藍色
            else:
                theplot[count].background_fill_color = "#B2DFDB" #綠色

          
            therow.append(theplot[count])
            count= count+1
        thecolumn.append(row(therow))
    return column(thecolumn)


        
#檢查當有任何選單、拉鍊被觸動時，觸發變動
def update(attr, old, new):
    layout.children[1] = update_plot()
    
for w in [x_axis, y_axis]:
    w.on_change('value', update)

# 畫布與選單編排
layout = row(column(x_axis, y_axis),column(update_plot()), width=2000)
curdoc().add_root(layout)
curdoc().title = "RFM_INT"
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:16:36 2019

@author: Ivan
"""
from os.path import dirname, join
import pandas as pd
from bokeh.io import curdoc
from math import pi
from bokeh.plotting import figure
from bokeh.layouts import row, column
from bokeh.transform import cumsum
# 設定資料
insurance = pd.read_csv(join(dirname(__file__), "insurance.csv"), encoding='utf-8')

#設定顏色
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

#繪製圓餅圖
def makeCircle_plot(df):
    therow=[] 
    thecolumn = []
    for i in range(len(df.columns)):
        if len(df) > len(df[df.columns[i]].value_counts()) and len(Spectral11) > len(df[df.columns[i]].value_counts()):
            data = df[df.columns[i]].value_counts().reset_index(name='value').rename(columns={'index':'class'})
            data['angle'] = data['value']/data['value'].sum() * 2*pi
            data['color'] = Spectral11[:len(data)]
            data['percent'] = ((data['value']/data['value'].sum()*10000).astype(int)/100).astype(str) + ' ％'
            
            theplot=figure(plot_height=350, title=df.columns[i], toolbar_location=None,
                       tools="hover", tooltips=[("數量", "@value"),("百分比","@percent")], x_range=(-0.5, 1.0))
            
            theplot.wedge(x=0, y=1, radius=0.4,
                    start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
                    line_color="white", fill_color='color', legend='class', source=data)
            
            theplot.axis.axis_label=None
            theplot.axis.visible=False
            theplot.grid.grid_line_color = None

            #讓圖片兩個一排
            if len(therow) > 1:
                thecolumn.append(row(therow))
                therow=[]
                therow.append(theplot)
            else:
                therow.append(theplot)
    if len(therow) != 0:
        thecolumn.append(row(therow))
    return column(thecolumn)


makeCircle_plot(insurance)    
   
# 畫布與選單編排
layout = column(
        row(makeCircle_plot(insurance))
        )



curdoc().add_root(layout)
curdoc().title = "Ivan_Circle"
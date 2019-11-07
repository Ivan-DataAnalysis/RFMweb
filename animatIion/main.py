# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:16:36 2019

@author: Ivan
"""
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource, Label, SingleIntervalTicker, Slider, HoverTool
from bokeh.models.widgets import Button
from data import make_data

# 設定資料
df = make_data()

#拉鍊設定
years = df['年分'].value_counts().index.sort_values()



year_Slider = Slider(start=years[0], end=years[-1], value=years[0], title="年分")
year_button = Button(label='► Play', width=60)
    
year = year_Slider.value
plot=figure(plot_width=1170,plot_height=700, title='動態點陣圖',
                                  x_range=(0, 1200),
                                  y_range=(0, 1200)
                                  )
plot.xaxis.ticker = SingleIntervalTicker(interval=100)
plot.xaxis.axis_label = "價值"
plot.yaxis.ticker = SingleIntervalTicker(interval=200)
plot.yaxis.axis_label = "價格"

source = ColumnDataSource(data=df[df['年分']==year])
plot.circle(x='價值', 
           y='價格', 
           size='市佔率', 
           color='顏色', 
           line_color='white', 
           hover_alpha=0.5, 
           alpha=0.6,
           source=source)

label = Label(x=1.1, y=18, text=str(year), text_font_size='70pt', text_color='#eeeeee')
plot.add_layout(label)



        
#檢查當有任何選單、拉鍊被觸動時，觸發變動
def slider_update(attrname, old, new):
    year = year_Slider.value
    label.text = str(year)
    sdf = df[df['年分']==year]
    if len(sdf) != 0:
        data = dict({})
        for x in sdf.columns:
            data[x]=sdf[x]
        source.data = data
 
##### 動畫部分
def animate_update():
    years = df['年分'].value_counts().index.sort_values()
    year = year_Slider.value + 1
    if year > years[-1]:
        year = years[0]
    year_Slider.value = year

def animate():
    global callback_id
    if year_button.label == '► Play':
        year_button.label = '❚❚ Pause'
        callback_id = curdoc().add_periodic_callback(animate_update, 200)
    else:
        year_button.label = '► Play'
        curdoc().remove_periodic_callback(callback_id)
        

year_button.on_click(animate)
year_Slider.on_change('value', slider_update)
# 畫布與選單編排
layout = column(
        row(year_Slider,year_button),
        row(plot  , width=1200, height=900))
        

curdoc().add_root(layout)
curdoc().title = "Ivan_Circle"
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:16:36 2019

@author: Ivan
"""
from os.path import dirname, join
import pandas as pd
from bokeh.io import show, curdoc
from bokeh.layouts import widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import DataTable, TableColumn, HTMLTemplateFormatter
# 設定資料
insurance = pd.read_csv(join(dirname(__file__), "insurance.csv"), encoding='utf-8')

data = dict({})
for x in insurance.columns:
    data[x]=insurance[x]

template="""
<div style="background:<%= 
    (function colorfromint(){
        if( value < 0){
            return("red")}
        else if( value > 1000000000){
            return("#00FA9A")}
        else if( value > 100000000){
            return("#ADFF2F")}
        else if( value > 10000000){
            return("#7CFC00")}
        else if( value > 1000000){
            return("#7FFF00")}
        else if( value > 100000){
            return("#00FF00")}
        else if( value > 10000){
            return("#32CD32")}
        else if( value > 1000){
            return("#9ACD32")}
        else if( value > 100){
            return("#8FBC8F")}
        else if( value > 90){
            return("#3CB371")}
        else if( value > 80){
            return("#66CDAA")}
        else if( value > 70){
            return("#20B2AA")}
        else if( value > 60){
            return("#008080")}
        else if( value > 50){
            return("#2E8B57")}
        else if( value > 40){
            return("#228B22")}
        else if( value > 30){
            return("#006400")}
        else if( value > 20){
            return("#808000")}
        else if( value > 10){
            return("#556B2F")}
        else if( value > 0){
            return("#2F4F4F")}
        }()) %>; 
    color: #FFFFFF"> 
<%= value %>
</div>
"""
formatter =  HTMLTemplateFormatter(template=template)


columns = [TableColumn(field=x, title=x, formatter=formatter) for x in insurance.columns ]
data_table = DataTable(source=ColumnDataSource(data), columns=columns, width=2000, height=800)

curdoc().add_root(widgetbox(data_table))
curdoc().title = "Ivan_Table"

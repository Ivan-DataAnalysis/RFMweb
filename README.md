RFM顧客資料透視
=========

`此專案目的只為了學術技術分享，請勿拿來從事不法行為，違者自行負起法律責任`

以Python套件bokeh實作出RFM動態網頁。
<img src="https://imgur.com/undefined.png"/>

目錄
=================
* [事前必要準備](#事前必要準備)
* [How to Use](#HowtoUse)
* [檔案說明](#檔案說明)
    * [showTable](#showTable)
    * [showCricle](#showCricle)
    * [animatIion](#animatIion)
    * [forSTR](#forSTR)
    * [forINT](#forINT)
   
 
事前必要準備
=================
1. 必須要下載bokeh套件 `pip install bokeh`。

How to Use
=================
1. 打開console介面，MAC電腦請開啟Ternimel，範例圖片是windows作業系統，以Anaconda prompt開啟。
<img src="https://imgur.com/Bib3wFr.png"/>

2. 複製此專案的位置，並且切換至此。 `cd 檔案路徑`。
<img src="https://imgur.com/4EwcRcs.png"/>

3. 輸入 `bokeh serve 專案資料夾名稱` 開始執行server，若沒有修改資料夾名稱，那指令會是 `bokeh serve showTable`。
<img src="https://imgur.com/zHpOJ3X.png"/>

4. 在網頁輸入 `http://localhost:5006/` ，即可進入server網頁。
<img src="https://imgur.com/AIZtbQ2.png"/>

檔案說明
=================


### showTable
實作將csv檔案在網頁上以表格的方式呈現，並且依顏色區隔數字大小。

| 檔案名稱      | 說明     |
| ---------- | :-----------:  |
| templates/index.html     | 設定html格式，裏頭只有增加css樣式。     |
| insurance.csv     | 在網頁中呈現的資料。     |
| main.py     | Python程式碼，bokeh套件的功能都寫在這裡。     |
| theme.yaml     | bokeh server的環境設定檔案，主要是修改主題相關顏色。     |
<img src="https://imgur.com/AIZtbQ2.png"/>

### showCricle
將所有的資料，全部都自動以圓餅圖展現出來，並且滑鼠移到上方，能顯示其百分比與真實數量。

| 檔案名稱      | 說明     |
| ---------- | :-----------:  |
| templates/index.html     | 設定html格式，裏頭只有增加css樣式。     |
| insurance.csv     | 在網頁中呈現的資料。     |
| main.py     | Python程式碼，bokeh套件的功能都寫在這裡。     |
| theme.yaml     | bokeh server的環境設定檔案，主要是修改主題相關顏色。     |
<img src="https://imgur.com/1WEmP4g.png"/>

### animatIion
利用網頁動畫，讓品牌的GPS市場定位圖活起來，馬上讓您知道公司位於市場的何處，與競爭對手的距離一目瞭然。

| 檔案名稱      | 說明     |
| ---------- | :-----------:  |
| templates/index.html     | 設定html格式，裏頭只有增加css樣式。     |
| data.py     | 創造資料。     |
| main.py     | Python程式碼，bokeh套件的功能都寫在這裡。     |
| theme.yaml     | bokeh server的環境設定檔案，主要是修改主題相關顏色。     |
<img src="https://imgur.com/ijmEuvd.png"/>

### forSTR
以保險業為例，製作類別型資料的RFM Model。

| 檔案名稱      | 說明     |
| ---------- | :-----------:  |
| templates/index.html     | 設定html格式，裏頭只有增加css樣式。     |
| cut_dataframe.py     | 切割RFM資料。     |
| insurance.csv     | 在網頁中呈現的資料。     |
| main.py     | Python程式碼，bokeh套件的功能都寫在這裡。     |
| theme.yaml     | bokeh server的環境設定檔案，主要是修改主題相關顏色。     |
<img src="https://imgur.com/eIzTnxB.png"/>

### forINT
以保險業為例，製作數值型資料的RFM Model。

| 檔案名稱      | 說明     |
| ---------- | :-----------:  |
| templates/index.html     | 設定html格式，裏頭只有增加css樣式。     |
| cut_dataframe.py     | 切割RFM資料。     |
| insurance.csv     | 在網頁中呈現的資料。     |
| main.py     | Python程式碼，bokeh套件的功能都寫在這裡。     |
| theme.yaml     | bokeh server的環境設定檔案，主要是修改主題相關顏色。     |
<img src="https://imgur.com/qVAmGXI.png"/>

FB文章自動分享社團
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
基本上分類資料夾內的檔案編排都是如下。

| 檔案名稱      | 說明     |
| ---------- | :-----------:  |
| templates/index.html     | 設定html格式，裏頭只有增加css樣式。     |
| insurance.csv     | 在網頁中呈現的資料。     |
| main.py     | Python程式碼，bokeh套件的功能都寫在這裡。     |
| theme.yaml     | bokeh server的環境設定檔案，主要是修改主題相關顏色。     |

### showTable
實作將csv檔案在網頁上以表格的方式呈現，並且依顏色區隔數字大小。
<img src="https://imgur.com/AIZtbQ2.png"/>

### showCricle
實作將csv檔案在網頁上以圓餅圖的方式呈現，只抓取資料欄為中為數值欄位的資料。
<img src="https://imgur.com/1WEmP4g.png"/>

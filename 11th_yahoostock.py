#(  )pandas, pandas_datareader, matplotlib.pyplot, 

#---------------------------------------------------始めていきましょう！
#---参考     https://qiita.com/innovation1005/items/5be026cf7e1d459e9562
#---参考　　　https://note.nkmk.me/python-pandas-datareader-stock-population/ #$ pip install pandas-datareader
# 公式ドキュメントによると、バージョン0.8.0時点では以下のデータソースがサポートされている。
# Tiingo
# IEX
# Alpha Vantage
# Enigma
# Quandl
# St.Louis FED (FRED)
# Kenneth French's data library
# World Bank
# OECD
# Eurostat
# Thrift Savings Plan
# Nasdaq Trader symbol definitions
# Stooq
# MOEX
# ----
# 

import datetime

import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# with open('data/temp/alpha_vantage_api_key.txt') as f:
#     api_key = f.read()

# start = datetime.datetime(2015, 1, 1)
# end = datetime.datetime(2019, 12, 31)

# df_sne = web.DataReader('SNE', 'av-daily', start, end, api_key=api_key)
# print(df_sne)
# print("以上です。ーーーーーーーーーーーーーーーーーーーーーー")

# # 
# # 
# # 
# # 
# # 
# # 
# # #---python3 /Users/knospear/Downloads/MyPython/11th#1_BS+yahoostock.py
# # -*- coding: utf-8 -*-
# import datetime
# # import pandas as pd
# #5th-要素のCSSスタイルを変更しようとしています（例：from "visibility: hidden;"から"visibility: visible;"）
# from selenium import webdriver #No module named selenium
# import chromedriver_binary #5th%1- pip install バージョン
# #pip install chromedriver-binary==87.0.4280.88.0 
# import time #5th%1
# #DateTime #4th
# import datetime #4th
# #---------------------->check https://docs.python.org/ja/3/library/datetime.html
# #driver = webdriver.Firefox()
# #driver.get("http://www.google.com")
# #driver.execute_script("document.getElementById('lga').style.display = 'none';")
# from bs4 import BeautifulSoup #1st
# import requests #1st
# #setting-mail #5th
# import smtplib #5th
# from email.mime.text import MIMEText #5th
# from email.utils import formatdate #5th
# import ssl #5th
# # ---------------------------------------------------------------------------
# setting_10th = 'Yahoo Finance USから株価をダウンロードしてみた'
# setting_url = 'https://qiita.com/innovation1005/items/5be026cf7e1d459e9562'

#代表的なナスダック100指数を構成する銘柄---------------------------------------
NDX=['AAL','AAPL','AMD','ALGN','ADBE','ADI','ADP','ADSK','ALXN','AMAT',
'AMGN','AMZN','ASML','ATVI','BIDU','BIIB','BMRN','BKNG','AVGO','CDNS',
'CERN','CHKP','CMCSA','COST','CSCO','CSX','CTAS','CTSH',
'CTXS','DLTR','EA','EBAY','EXPE','FAST','FB','FISV','FOX','FOXA',
'GILD','GOOG','GOOGL','HAS','HSIC','HOLX','IDXX','ILMN','INCY',
'INTC','INTU','ISRG','JBHT','JD','KHC','KLAC','LBTYB','LBTYA',
'LBTYK','LULU','LILA','LILAK','LRCX','MAR','MCHP','MELI','MNST',
'MSFT','MU','MXIM','MELI','MYL','NTAP','NFLX','NTES','NVDA','NXPI',
'ORLY','PAYX','PCAR','PYPL','PEP','QCOM','REGN','ROST','SBUX',
'SNPS','SIRI','SWKS','TMUS','TTWO','TSLA','TXN','KHC',
'ULTA','UAL','VRSN','VRSK','VRTX','WBA','WDC','WLTW','WDAY','XEL']

#代表的なダウ平均株価指数採用銘柄
DJ=['AAPL','AMGN','AXP','BA','CAT','CRM','CSCO','CVX','DIS','DOW','GS','HD',
    'IBM','INTC','JNJ','JPM','KO','MCD','MMM','MRK','MSFT','NKE',
    'PG','TRV','UNH','V','VZ','WBA','WMT']
#代表的な米国ETF
ETF=['DIA','SPY','QQQ','IBB','XLV','IWM','EEM','EFA','XLP','XLY','ITB','XLU','XLF',
     'VGT','VT','FDN','IWO','IWN','IYF','XLK','XOP','USMV','BAB','GLD',
    'VNQ','SCHH','IYR','XLRE','AGG','BND','LQD','VCSH','VCIT','JNK']
#代表的なS&P株
SP100=["AAPL","ABBV","ABT","ACN","AGN","AIG","ALL","AMGN","AMZN","AXP","BA","BAC","BIIB",
"BK","BLK","BMY","BRKB","C","CAT","CHTR","CL","CMCSA","COF","COP","COST","CSCO",
"CVS","CVX","DHR","DIS","DUK","EMR","EXC","F","FB","FDX","FOX","FOXA","GD","GE",
"GILD","GM","GOOG","GOOGL","GS","HAL","HD","HON","IBM","INTC","JNJ","JPM","KHC","KMI",
"KO","LLY","LMT","LOW","MA","MCD","MDLZ","MDT","MET","MMM","MO","MRK","MS","MSFT",
"NEE","NKE","ORCL","OXY","PEP","PFE","PG","PM","PYPL","QCOM","RTN","SBUX",
"SLB","SO","SPG","T","TGT","TXN","UNH","UNP","UPS","USB","UTX","V","VZ","WBA",
"WFC","WMT","XOM"]

#代表的なバイオ・ヘルス株
BIO=['GILD','VRTX','AMGN','BIIB','REGN','ILMN','SGEN','ALXN','INCY','BMRN','MRNA',
     'ALNY','SYN','NBIX','SRPT','EXEL','IONS','TECH','MYL','ACAD','NKTR','ALKS',
     'BLUE','JAZZ','QGEN','NBIX','SAGE','UTHR','ABBV','INO','VXRT']
HLT=['JNJ','UNH','MRK','PFE','ABT','BMY','AMGN','LLY','TMO','MDT','DHR','CVS','BDX',
     'VRTX','CI','ANTM','AGN','ISRG','ZTS','CERN','HSIC','HOLX','IDXX','MYL','WBA',
     'XRAY','ABBV']

#代表的な暗号通貨
# https://finance.yahoo.com/cryptocurrencies
ccurrency=["BTC-USD","XRP-USD","ETH-USD","LTC-USD","BCH-USD","BNB-USD",
       "EOS-USD","USDT-USD","LINK-USD","TRX-USD","ADA-USD",
       "XLM-USD","XMR-USD","DASH-USD","NEO-USD","IOT-USD",
       "VEN-USD","ETC-USD","XEM-USD","ZEC-USD","XRB-USD","QTUM-USD",
       "BTG-USD","BAT-USD","DOGE-USD"]
# ---------------------------------------------------------------------------
# 
#US Yahoo Financeのデータ構成
# Open:始値
# High:高値
# Low:安値
# Close:終値　-　分割調整後
# Volume:出来高
# Adj Close:配当込み分割調整後株価
# ETFとは上場投資信託のことで手数料の点で株式と同じ手数料で売買ができるために、通常の投資信託よりも費用の面で有利です。
# では実際にダウンロードしてみましょう。
# %matplotlib inline  #error:File "/Users/knospear/Downloads/MyPython/10th#1_BS+yahoostock.py", line 88
# import matplotlib.pyplot as plt #描画ライブラリ
# import pandas_datareader.data as web #データのダウンロードライブラリ
# tsd = web.DataReader("usmv","yahoo","1980/1/1").dropna()#jpy
# tsd.loc[:,'Adj Close'].plot()



# # ---------------------------------------------------------------------------
# #----------------------------------------ダウ工業株30種平均に採用されている銘柄をダウンロードしてリターンとリスクをみる
# import matplotlib.pylab as plt
# import seaborn as sns
# import pandas_datareader.data as web
# import pandas as pd
# #----------------------------------------ダウ工業株30種平均に採用されている銘柄をダウンロードしてリターンとリスクをみる
# m=[]#それぞれの株価の年率換算平均のデータを保存
# v=[]#それぞれの株価の年率換算した標準偏差を保存
# j=0
# for i in range(len(DJ)):
#     tsd=web.DataReader(DJ[i], "yahoo",'2010/1/1')#株価データのダウンロード
#     if len(tsd)>2000:
#         tsd2=web.DataReader(DJ[i], "yahoo",'1980/1/1','2009/12/31')#株価データのダウンロード
#         if len(tsd2)>1000:
#             lntsd=np.log(tsd.iloc[:,5])#データの自然対数を取る
#             m.append((lntsd.diff().dropna().mean()+1)**250-1)
#             v.append(lntsd.diff().dropna().std()*np.sqrt(250))
#             print('{0: 03d}'.format(j+1),'{0:7s}'.format(DJ[i]),'平均{0:5.2f}'.format(m[j]),
#               'ボラティリティ {0:5.2f}'.format(v[j]),'m/v {0:5.2f}'.format(m[j]/v[j]),
#               ' データ数{0:10d}'.format(len(tsd)))
#             j+=1
# v_m=pd.DataFrame({'v':v,'m':m})
# sns.jointplot(x='v',y='m',data=v_m,color="g")

# start = datetime.datetime(2015, 1, 1)
# end = datetime.datetime(2019, 12, 31)

# df_sne = web.DataReader('SNE', 'av-daily', start, end, api_key=api_key)
# print(df_sne)
#              open    high    low  close   volume
# 2015-01-02  20.47  20.685  20.43  20.56  1229939
# 2015-01-05  20.45  20.450  20.21  20.26  1083137
# 2015-01-06  20.46  20.580  20.15  20.25  2209124
# 2015-01-07  21.59  21.700  21.47  21.53  2486293
# 2015-01-08  21.53  21.620  21.47  21.56  1296471
# ...           ...     ...    ...    ...      ...
# 2019-12-24  67.98  68.000  67.76  67.76   264463
# 2019-12-26  68.00  68.030  67.85  68.02   517975
# 2019-12-27  68.03  68.100  67.73  67.78   351118
# 2019-12-30  67.78  67.790  67.25  67.72   993865
# 2019-12-31  67.72  68.025  67.51  68.00   549672
# 
# [1258 rows x 5 columns]

# df_aapl = web.DataReader('AAPL', 'av-daily', start, end, api_key=api_key)
# print(df_aapl)
#               open    high       low   close    volume
# 2015-01-02  111.39  111.44  107.3500  109.33  53204626
# 2015-01-05  108.29  108.65  105.4100  106.25  64285491
# 2015-01-06  106.54  107.43  104.6300  106.26  65797116
# 2015-01-07  107.20  108.20  106.6950  107.75  40105934
# 2015-01-08  109.23  112.15  108.7000  111.89  59364547
# ...            ...     ...       ...     ...       ...
# 2019-12-24  284.69  284.89  282.9197  284.27  12119714
# 2019-12-26  284.82  289.98  284.7000  289.91  23334004
# 2019-12-27  291.12  293.97  288.1200  289.80  36592936
# 2019-12-30  289.46  292.69  285.2200  291.52  36059614
# 2019-12-31  289.93  293.68  289.5200  293.65  25247625
# 
# [1258 rows x 5 columns]

# df_sne_aapl = pd.DataFrame({'≈': df_sne['close'], 'AAPL': df_aapl['close']})
# print(df_sne_aapl)
#               SNE    AAPL
# 2015-01-02  20.56  109.33
# 2015-01-05  20.26  106.25
# 2015-01-06  20.25  106.26
# 2015-01-07  21.53  107.75
# 2015-01-08  21.56  111.89
# ...           ...     ...
# 2019-12-24  67.76  284.27
# 2019-12-26  68.02  289.91
# 2019-12-27  67.78  289.80
# 2019-12-30  67.72  291.52
# 2019-12-31  68.00  293.65
# 
# [1258 rows x 2 columns]

# CSVで保存
#https://note.nkmk.me/python-pandas-datareader-stock-population/
# pandas.DataFrameのto_csv()メソッドでCSVファイルとして保存できる。
# 関連記事: pandasでcsvファイルの書き出し・追記（to_csv）

# df_aapl.to_csv('data/src/aapl_2015_2019.csv')
# df_sne_aapl.to_csv('data/src/sne_aapl_2015_2019.csv')

# グラフをプロット
# プロットするのも簡単。pandas.DataFrameのplot()メソッドを使う。
# 関連記事: pandasのplotメソッドでグラフを作成しデータを可視化
# Alpha Vantageで取得できるpandas.DataFrameのindexは文字列だが、これをpd.to_datetime()でDatetimeIndexに変換して時系列データとしておくとプロット時のX軸を適切に調整してくれる。
# print(type(df_sne_aapl.index))
# <class 'pandas.core.indexes.base.Index'>

# df_sne_aapl.index = pd.to_datetime(df_sne_aapl.index)
# print(type(df_sne_aapl.index))
# <class 'pandas.core.indexes.datetimes.DatetimeIndex'>

# df_sne_aapl.plot(title='SNE vs. AAPL', grid=True)
# plt.show()
# plt.savefig('data/dst/pandas_datareader_stock.png')
# plt.close()

#plt.savefig()は結果を画像ファイルとして保存する。表示させたい場合はplt.show()を使う。
# 期間の初日で規格化する例は以下の通り。
# df_sne_aapl['SNE'] /= df_sne_aapl['SNE'][0]
# df_sne_aapl['AAPL'] /= df_sne_aapl['AAPL'][0]

# df_sne_aapl.plot(title='SNE vs. AAPL', grid=True)
# plt.savefig('data/dst/pandas_datareader_stock_normalize.png')
# plt.close()

#107debba47b6c498a3b70ba25c03e928d9596ab2
print("TiingoDailyReaderーーーーーーーーーーーーーーーーーーーーーー")
from pandas_datareader.tiingo import TiingoDailyReader
print("from pandas_datareader.tiingo ーーーーーーーーーーーーーーーーーーーーーー")
x = TiingoDailyReader(["AAPL", "SPY"], #<pandas_datareader.tiingo.TiingoDailyReader object at 0x7fd7c06619a0>
     "2020-11-1", 
     "2020-12-11", 
     api_key="107debba47b6c498a3b70ba25c03e928d9596ab2") 

print("x.read()?")
datas=x.read()
print("x.read()?")
print(datas)
#                                   close    high  ...  divCash  splitFactor
# symbol date                                       ...                      
# AAPL   2020-01-02 00:00:00+00:00  300.35  300.60  ...      0.0          1.0
#        2020-01-03 00:00:00+00:00  297.43  300.58  ...      0.0          1.0
# SPY    2020-01-02 00:00:00+00:00  324.87  324.89  ...      0.0          1.0
#        2020-01-03 00:00:00+00:00  322.41  323.64  ...      0.0          1.0

print("x.read()!") 
print("上記で紹介した IEX は、彼ら謹製のLibraryも作っています。ーーーーーーーーーーーーーーーーーーーーーー")
# realtime データ取得
# 1データなら、数値で返ります。
# from iexfinance.stocks import Stock
# tsla = Stock('TSLA')

# print("tsla.get_price()ーーーーーーーーーーーーーーーーーーーーーー")
# print(str(tsla.get_price())+"ーーーーーーーーーーーーーーーーーーーーーー")
# # 326.09
# # 複数ある場合
# batch = Stock(["TSLA", "AAPL"])
# prices = batch.get_price()
# print(prices)
# # for oneprice in prices
# #      print(oneprice)


#Quandlも登録とAPIKey発行が必要です
#R-3EsDy1_tJZ4HTpgysC
# print("Quandlも登録とAPIKey発行が必要ですーーーーーーーーーーーーーーーーーーーーーー")
# from pandas_datareader.quandl import QuandlReader
# print("from pandas_datareader.quandl ーーーーーーーーーーーーーーーーーーーーーー")
# x = QuandlReader(['AAPL.US', 'SPY.US'],
#                 '2020-01-01', 
#                 '2020-01-10', 
#                 api_key="R-3EsDy1_tJZ4HTpgysC" )  
# print("x = QuandlReaderーーーーーーーーーーーーーーーーーーーーーー")
# x.read()
# print("x.read()ーーーーーーーーーーーーーーーーーーーーーー")

print("以上です。ーーーーーーーーーーーーーーーーーーーーーー")

#つぎにさらに長い期間のデータをダウンロードしてデータを分析してみましょう。


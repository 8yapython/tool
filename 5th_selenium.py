# -*- coding: utf-8 -*-
from selenium import webdriver #(1)WEB操作、学習中 :pip install 
import chromedriver_binary #(1)WEB操作、学習中
#pip install chromedriver-binary==87.0.4280.88.0 #バージョンをインストール済みChromeと合わせる
import time #(2)
import datetime #(2)
#driver = webdriver.Firefox() #(1)
#driver.get("http://www.google.com") #(1)
#driver.execute_script("document.getElementById('lga').style.display = 'none';") #(1)
#(0)Webスクレイピング、学習済
from bs4 import BeautifulSoup
import requests
#(0)メール、学習済
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import ssl
#----------------------------------------さぁ、始めましょう----------------------------------------------
#(0)メール、学習済
FROM_ADDRESS = '(指定する)'
MY_PASSWORD = '(指定する)'
TO_ADDRESS = '(指定する)'
BCC = '' 
SUBJECT = 'GmailのSMTPサーバ経由'
#mail　body
BODY = 'pythonでメール送信 \n'
#ファイル記入内容をメール送信ーーーーーーーー追加
f = open("(指定する)/xx.txt","r") #★変更可能 #r:read
for line in f:
    print(line)
    BODY += '\n'+line


def create_message(from_addr, to_addr, bcc_addrs, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Bcc'] = bcc_addrs
    msg['Date'] = formatdate()
    
   

    msg['Body'] = body

    return msg


def send(from_addr, to_addrs, msg):
    #context = ssl.create_default_context()
    smtpobj = smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10)
    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()

#メール送信をする ~send
if __name__ == '__main__':

    to_addr = TO_ADDRESS
    subject = SUBJECT
    body = BODY

    msg = create_message(FROM_ADDRESS, to_addr, BCC, subject, body)
    send(FROM_ADDRESS, to_addr, msg,) #以上です。


#DateTime
now = datetime.datetime.now()
#now.year+

#file
f = open("(指定する)/(フォルダ名))"+str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second)+".html","a")
# f.write(str(now))
#以上です。27get

#1st.
#URLを受け取りhtmlを返す
def url_to_soup(url):
    # レスポンスオブジェクトを取得
    response = requests.get(url)
    # encoding=>utf-8
    response.encoding = response.apparent_encoding
    # レスポンステキストを変数htmlに格納
    html=response.text
    # BeautifulSoupをhtml形式テキストで初期化、
    return BeautifulSoup(html, 'html.parser') # BeautifulSoupの初期化


#url="https://ja.wikipedia.org/wiki/メインページ"
url="https://ja.wikipedia.org/wiki/特別:新しいページ"
# url=""
# url=""
# url=""
#soup=url_to_soup(url) # url文字列からhtml形式テキスト返却
#f.write(str(soup))



#myEDIT.
#mw-parser-output #<p><a> #<----*これをstyle="opacity:0.5;"---->
#mw-parser-output #<p><a> #<----*これをstyle="opacity:1;"---->
#mw-parser-output #<p><a> #<----*これをstyle="onClick=class"---->
# driver = webdriver.Chrome()
# driver.get('https://www.google.com/')
# time.sleep(2)
# search_box = driver.find_element_by_name("q")
# #search_box.send_keys('ChromeDriver')
# search_box.send_keys('クイズ 2020年12月')
# search_box.submit()
# time.sleep(600)
# driver.quit()
# driver = webdriver.Chrome()
# driver.get("http://www.google.com")
# driver.execute_script("document.getElementById('lga').style.display = 'none';")



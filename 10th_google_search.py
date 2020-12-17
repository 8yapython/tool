#(1)search_box.send_keys ...Google検索をする
#(2)mailbody+=           ...検索結果からメール本文を作成
#(3)smtpobj.sendmail     ...メールを送信する
#---------------------------------------------------始めていきましょう！
# -*- coding: utf-8 -*-
import datetime
from selenium import webdriver #No module named selenium
import chromedriver_binary #学習済-5th
#pip install chromedriver-binary==87.0.4280.88.0 
import time #学習済-5th
import datetime #学習済-4th
#---------------------->check https://docs.python.org/ja/3/library/datetime.html
#driver = webdriver.Firefox()
#driver.get("http://www.google.com")
#driver.execute_script("document.getElementById('lga').style.display = 'none';")
from bs4 import BeautifulSoup #学習済-1st
import requests #学習済-1st
#setting-mail #5th
import smtplib #学習済-5th
from email.mime.text import MIMEText #学習済-5th
from email.utils import formatdate #学習済-5th
import ssl #学習済-5th
# ---------------------------------------------------------------------------v
setting_10th = '玄米 トースター'

interval = 1
#10th-以下、
#myEDIT.
#mw-parser-output #<p><a> #<----*これをstyle="opacity:0.5;"---->
#mw-parser-output #<p><a> #<----*これをstyle="opacity:1;"---->
#mw-parser-output #<p><a> #<----*これをstyle="onClick=class"---->
driver = webdriver.Chrome()
driver.get('https://www.google.com/')
search_box = driver.find_element_by_name("q")
search_box.send_keys(setting_10th)
search_box.submit()
time.sleep(interval)


#setting-mail
mailbody=''
#検索結果の一覧を取得する　〜driver.close
results = []
flag = False
#日付を取得
nowObj = datetime.datetime.now()
now =  nowObj.strftime('%Y年%m月%d日%H時%M分')
#now =  str(nowObj.year)+'年'+str(nowObj.month)+'月'+str(nowObj.day)+'日'+str(nowObj.hour)+'時'+str(nowObj.minute)+'分'
print(now)

no=1
while True:

    g_ary = driver.find_elements_by_class_name('g')
    for g in g_ary:
        result = {}
        result['url'] = g.find_element_by_class_name('yuRUbf').find_element_by_tag_name('a').get_attribute('href')
        result['title'] = g.find_element_by_tag_name('h3').find_element_by_tag_name('span').text
        print(now+'-'+str(no)+'-------------\n')#改行\n
        mailbody+=now+'-'+str(no)+'-------------\n'
        mailbody+=result['title']+'\n'
        mailbody+=result['url']+'\n\n'
        no += 1
        print(result['title']+'-------------\n')
        print(result['url']+'-------------\n')
    
        results.append(result)
    if len(results) >= 50:
        flag = True
        break
    if flag:
        break
        driver.find_element_by_id('pnnext').click()#time.sleep(30)へ。#検索結果の一覧を取得する



#メール送信をする ~send
#setting-mail
#mail
FROM_ADDRESS = '(指定する)'
MY_PASSWORD = '(指定する)'
TO_ADDRESS = '(指定する)'
BCC = ''
SUBJECT = "MyPython:"+setting_10th #検索ワード
BODY = mailbody
#return msg
def create_message(from_addr, to_addr, bcc_addrs, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Bcc'] = bcc_addrs
    msg['Date'] = formatdate()
    msg['Body'] = body
    return msg
#smtpobj.sendmail    
def send(from_addr, to_addrs, msg):
    #context = ssl.create_default_context()
    smtpobj = smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10)
    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()
if __name__ == '__main__':
    to_addr = TO_ADDRESS
    subject = SUBJECT
    body = BODY
    msg = create_message(FROM_ADDRESS, to_addr, BCC, subject, body)
    send(FROM_ADDRESS, to_addr, msg,) #以上です。
    #------------------------------------------------10th

countDown=30
while countDown > 0:
    print(countDown) #1秒カウントダウン、ログ表示をしています
    countDown -= 1
    time.sleep(1)
time.sleep("driver.close()")
#time.sleep(30)
driver.close()#以上です。#検索結果の一覧を取得する


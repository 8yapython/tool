# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup #(1)Webスクレイピング用
import requests #(1)Webスクレイピング用
#mail
import smtplib #(2)メール送信用
from email.mime.text import MIMEText #(2)メール送信用
from email.utils import formatdate #(2)メール送信用
import ssl #(2)メール送信用
#DateTime
import datetime 

#(2)メール送信用
FROM_ADDRESS = 'your_mail@xxxx.xxx'
MY_PASSWORD = 'your_password'
TO_ADDRESS = 'send_to@xxxx.xxx'
BCC = ''
SUBJECT = 'GmailのSMTPサーバ経由'
BODY = 'pythonでメール送信'


def create_message(from_addr, to_addr, bcc_addrs, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Bcc'] = bcc_addrs
    msg['Date'] = formatdate()
    return msg


def send(from_addr, to_addrs, msg):
    #context = ssl.create_default_context()
    smtpobj = smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10)
    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()


# if __name__ == '__main__':

#     to_addr = TO_ADDRESS
#     subject = SUBJECT
#     body = BODY

#     msg = create_message(FROM_ADDRESS, to_addr, BCC, subject, body)
#     send(FROM_ADDRESS, to_addr, msg)


#DateTime
now = datetime.datetime.now()
#now.year+

#file
f = open("(ローカルパス)"+str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second)+".html","a")
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
soup=url_to_soup(url) # url文字列からhtml形式テキスト返却
f.write(str(soup))

# #記事タイトルタグを検索し、
# tags=soup.find_all("li", {"class":"archive-list-item"})
# titles=[]

# index=0
# # タイトル変数に格納
# for tag in tags:
#     titles.append(tag.a.string)
#     print(str(index+1)+":"+titles[index])
#     index+=1
#     if (index==20):
#         break

# print("-----------------------")
# selected_number=int(input("コメントを取得する記事の番号を入力:"))
# # 記事 URLに指定番号を付与
# selected_page_URL=tags[selected_number-1].a.get("href")
# selected_soup=url_to_soup(selected_page_URL)
# # 記事詳細ページからコメントタグを全て取得
# selected_tags=selected_soup.find_all("div",{"class":"comment-content"})

#myEDIT.
#mw-parser-output #<p><a> #<----*これをstyle="opacity:0.5;"---->
#mw-parser-output #<p><a> #<----*これをstyle="opacity:1;"---->
#mw-parser-output #<p><a> #<----*これをstyle="onClick=class"---->


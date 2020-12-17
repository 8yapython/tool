#webページの記事タイトルを抜き出して、特定の記事にアクセスして「コメント」を抜き出す
#1stwebページ読み込み
from bs4 import BeautifulSoup
import requests

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


url="http://digicame-info.com/archives.html" #サンプルHTML
soup=url_to_soup(url) # url文字列からhtml形式テキスト返却
#記事タイトルタグを検索し、
tags=soup.find_all("li", {"class":"archive-list-item"})
titles=[]

index=0
# タイトル変数に格納
for tag in tags:
    titles.append(tag.a.string)
    print(str(index+1)+":"+titles[index])
    index+=1
    if (index==20):
        break

print("-----------------------")
selected_number=int(input("コメントを取得する記事の番号を入力:"))
# 記事 URLに指定番号を付与
selected_page_URL=tags[selected_number-1].a.get("href")
selected_soup=url_to_soup(selected_page_URL)
# 記事詳細ページからコメントタグを全て取得
selected_tags=selected_soup.find_all("div",{"class":"comment-content"})

comments=[]
index=0

for selected_tag in selected_tags:
    comment=selected_tag.p.text
    comments.append(comment)
    print("・"+comments[index])
    print(" ")
    index+=1



#以上です。
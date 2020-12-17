#2nd_youtube...こちらはwebスクレイピングエラー確認用zsです。


#ライブラリのネーミング
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
    #print("url_to_soup:"+html)
    # BeautifulSoupをhtml形式テキストで初期化、
    return BeautifulSoup(html, 'html.parser') # BeautifulSoupの初期化


url="http://digicame-info.com/archives.html"
home="https://www.youtube.com/feed/"
trend="https://www.youtube.com/feed/trending"
#metadata-line  span 253万 回視聴 span 
# a#video-title title
# #search [英語][python][corona virus]

myHome=url_to_soup(home) # url文字列からhtml形式テキスト返却
yourTrend=url_to_soup(trend) # url文字列からhtml形式テキスト返却
#記事タイトルタグを検索し、
titleTags=yourTrend.find_all("a")#("a", {"id":"video-titl"})
#print("titleTags:"+str(titleTags))
metaTags=yourTrend.find_all("div", {"id":"metadata-line"})
titles=[]

index=0
# タイトル変数に格納
for titleTag in titleTags:
    titles.append(str(titleTag.get("href")))#< title="...">  #a.stringから変更
    print(str(index+1)+":"+titles[index])
    index+=1
    if (index==25):
        break
# (base) knospear@MacBook-Air MyPython % 
# 1:https://www.youtube.com/about/
# 2:https://www.youtube.com/about/press/
# 3:https://www.youtube.com/about/copyright/
# 4:/t/contact_us
# 5:https://www.youtube.com/creators/
# 6:https://www.youtube.com/ads/
# 7:https://developers.google.com/youtube
# 8:/t/terms
# 9:https://www.google.co.jp/intl/ja/policies/privacy/
# 10:https://www.youtube.com/about/policies/
# 11:https://www.youtube.com/howyoutubeworks?utm_campaign=ytgen&utm_source=ythp&utm_medium=LeftNav&utm_content=txt&u=https%3A%2F%2Fwww.youtube.com%2Fhowyoutubeworks%3Futm_source%3Dythp%26utm_medium%3DLeftNav%26utm_campaign%3Dytgen
# 12:/new
# (base) knospear@MacBook-Air MyPython % 

# print("-----------------------")
# selected_number=int(input("コメントを取得する記事の番号を入力:"))
# # 記事 URLに指定番号を付与
# selected_page_URL=tags[selected_number-1].a.get("href")
# selected_soup=url_to_soup(selected_page_URL)
# # 記事詳細ページからコメントタグを全て取得
# selected_tags=selected_soup.find_all("div",{"class":"comment-content"})

# comments=[]
# index=0

# for selected_tag in selected_tags:
#     comment=selected_tag.p.text
#     comments.append(comment)
#     print("・"+comments[index])
#     print(" ")
#     index+=1



#以上です。
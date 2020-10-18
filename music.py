import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost',27017) #host
db = client.myMusic

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 아래 빈 칸('')을 채워보세요
#requests
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
#bs4
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
# 아래 빈 칸('')을 채워보세요
for tr in trs:
    rank = tr.select_one('td.number').text[0:2].strip()
    title = tr.select_one('a.title.ellipsis').text.strip()
    artist = tr.select_one('a.artist.ellipsis').text

 #pymongo를 사용해서 data 저장하기
    music_dict = {
       'rank':rank,
        'title':title,
        'artist':artist
    }

    db.gmusic.insert_one(music_dict)
    print("저장 >>>", rank, title, artist)
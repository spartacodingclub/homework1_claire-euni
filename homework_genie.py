import requests
from bs4 import BeautifulSoup


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309', headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')
list = soup.select('tr>td.info')

rank = 0
for song in list:
    title_el = song.select('a.title')
    artist_el = song.select('a.artist')
    if len(title_el) > 0:
        rank += 1
        title_name = title_el[0].text.strip()
        artist_name = artist_el[0].text.strip()

        print(rank, title_name, '-', artist_name)
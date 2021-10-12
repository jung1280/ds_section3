from bs4 import BeautifulSoup as bs
from selenium import webdriver


#가요 / 댄스 - L0102, 가요 / 랩/힙합 - L0104, 가요 / 발라드 - L0101, OST / 드라마 - L0301, POP / 팝 - L0201, 가요 / 락 - L0105

#body-content > div.songlist-box > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis -> 노래제목
#body-content > div.songlist-box > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis -> 아티스트 이름
#body-content > div.songlist-box > div > table > tbody > tr:nth-child(1) > td.info > a.albumtitle.ellipsis -> 앨범 이름


def song_recommend(pred_genre):

    import random

    if pred_genre == '가요 / 댄스':

        pred_genre = 'L0102'

    elif pred_genre == '가요 / 랩/힙합':

        pred_genre = 'L0104'

    elif pred_genre == '가요 / 발라드':

        pred_genre = 'L0101'    

    elif pred_genre == 'OST / 드라마':

        pred_genre = 'L0301'

    elif pred_genre == 'POP / 팝':

        pred_genre = 'L0201'

    elif pred_genre == '가요 / 락':

        pred_genre = 'L0105'

    options = webdriver.ChromeOptions()
    options.add_argument("headless")


    driver = webdriver.Chrome(r'C:\Users\wjdrl\project3\chromedriver.exe', options=options)
    url = f'https://www.genie.co.kr/genre/{pred_genre}'


    driver.get(url)
    
    html = driver.page_source
    soup = bs(html, 'html.parser')

    title_list = []
    artist_list = []
    album_list = []

    for i in random.sample(range(1, 31), 20):



        title = soup.select(f'#body-content > div.songlist-box > div > table > tbody > tr:nth-child({i}) > td.info > a.title.ellipsis')[0].text.lstrip()
        artist = soup.select(f'#body-content > div.songlist-box > div > table > tbody > tr:nth-child({i}) > td.info > a.artist.ellipsis')[0].text.lstrip()
        album = soup.select(f'#body-content > div.songlist-box > div > table > tbody > tr:nth-child({i}) > td.info > a.albumtitle.ellipsis')[0].text.lstrip()
    
        title_list.append(title)
        artist_list.append(artist)
        album_list.append(album)

    driver.quit()

    return title_list, artist_list, album_list






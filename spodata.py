import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import random


def chart_list(chart_url='https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=', start_date='20201005', end_date='20211005'):

    header = {'User-Agent': 'Mozilla/5.0'}
    song_list = []
    artist_list = []
    time_list = []

    while True:

        chart_url=f'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd={start_date}'


        chart = requests.get(chart_url, headers=header)
        chart_data = BeautifulSoup(chart.content, 'html.parser')

        chart_song = chart_data.find_all('a', class_ = 'title ellipsis')
        chart_artist = chart_data.find_all('a', class_ = 'artist ellipsis')

        for i in chart_song:

            song_list.append(str(i.text).lstrip())
            h_d = datetime.strptime(start_date, '%Y%m%d')
            time_list.append(datetime.strftime(h_d, '%Y-%m-%d'))

        for j in chart_artist:

            artist_list.append(str(j.text).lstrip())

        s_d = datetime.strptime(start_date, '%Y%m%d')
        t_d = s_d + timedelta(days=1)  

        c = datetime.strftime(t_d, '%Y-%m-%d')
        a = c.split('-')
        h = a[0] + a[1] + a[2]

        start_date = h

        if start_date == end_date:

            break

    return song_list, artist_list, time_list

def genre(song_list, artist_list):

    song = song_list
    artist = artist_list
    genre_list = []

    for i in range(0, len(song)):

        header = {'User-Agent': 'Mozilla/5.0'}
        song_url = f'https://www.genie.co.kr/search/searchMain?query={song[i]}+{artist[i]}'

        res = requests.get(song_url, headers=header)
        soup = BeautifulSoup(res.content, 'html.parser')

        a1 = soup.find_all('tbody')[0]

        a2 = a1.find('tr', class_='list')
        song_id = str(a2)[25:33]

        genre_url = f'https://www.genie.co.kr/detail/songInfo?xgnm={song_id}'

        res2 = requests.get(genre_url, headers=header)

        soup2 = BeautifulSoup(res2.content, 'html.parser')

        c1 = soup2.find_all('span', class_='value')[2]
        c2 = c1.text

        genre_list.append(c2)

    return  genre_list

song_list, artist_list, time_list = chart_list(start_date='20210925', end_date='20211005')

genre_list = genre(song_list, artist_list)

track_df = pd.DataFrame(data = {'time': time_list, 'track_name': song_list, 'genre': genre_list}) 


def select_genre(df, start_date='2020-10-05', end_date='2021-10-05'):

    df = df.groupby(['time', 'genre']).count().stack()
    time_list = []
    genre_list = []
    genre_value_list = []

    while True:

        time_list.append(start_date)        
        data = df[f'{start_date}'].nlargest(3).index.tolist()

        for i in data:

            genre_list.append(i[0])

        genre_value = random.sample(genre_list, 1)[0]

        s_d = datetime.strptime(start_date, '%Y-%m-%d')
        t_d = s_d + timedelta(days=1)

        start_date = datetime.strftime(t_d, '%Y-%m-%d')
        genre_value_list.append(genre_value)

        if start_date == end_date:

            break
    
    genre_df = pd.DataFrame(data = {'time': time_list, 'selected_genre': genre_value_list})
    
    return genre_df

track_genre_df = select_genre(track_df, start_date='2021-09-25', end_date='2021-10-05')


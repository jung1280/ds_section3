import psycopg2
from weather import weather_df
from spodata import track_genre_df
import pandas as pd

data = pd.merge(weather_df, track_genre_df, how='inner', on='time')

def collect_data(data):

    host = ''
    user = ''
    password = ''
    database = '' # db 정보

    conn = psycopg2.connect(host=host
                                , user=user
                                , password=password
                                , database=database)

    cur = conn.cursor()

    #cur.execute('DROP TABLE IF EXISTS track_weather;')

    #cur.execute('CREATE TABLE track_weather(time VARCHAR(120) PRIMARY KEY, temp FLOAT, cloud INTEGER, rain FLOAT, weather VARCHAR(120), selected_genre VARCHAR(120));')

    for i in range(len(data)):

        a = data.iloc[i, :]
        b = (a['time'],) + (a['temp'],) + (int(a['cloud']),) + (a['rain'],) + (a['weather'],) + (a['selected_genre'],)

        cur.execute('INSERT INTO track_weather(time, temp, cloud, rain, weather, selected_genre) VALUES (%s, %s, %s, %s, %s, %s)', b)

    print('Data 수집 성공!!')
    conn.commit()
# 20201005 ~ 20201105(O)
# 20201105 ~ 20201125(O)
# 20201125 ~ 20201215(O)
# 20201215 ~ 20210105(O)
# 20210105 ~ 20210125(O)
# 20210125 ~ 20210215(O)
# 20210215 ~ 20210305(O)
# 20210305 ~ 20210325(O)
# 20210325 ~ 20210415(O)
# 20210415 ~ 20210505(O)
# 20210505 ~ 20210525(O)
# 20210525 ~ 20210615(O)
# 20210615 ~ 20210705(O)
# 20210705 ~ 20210725(O)
# 20210725 ~ 20210815(O)
# 20210815 ~ 20210905(O)
# 20210905 ~ 20210925(O)
# 20210925 ~ 20211005(O)

#collect_data(data)

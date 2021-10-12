import requests
import json
from datetime import datetime, timedelta
import pandas as pd

enkey = 'fIPYKzDq5zQKFl0y6cgkUxrIAeKvCjx13wrgGUpQNkQYCRZV6gke%2BLsQakTx%2FktQRETepj%2FxvHuqHKJzoRzSvQ%3D%3D'
dekey = 'fIPYKzDq5zQKFl0y6cgkUxrIAeKvCjx13wrgGUpQNkQYCRZV6gke+LsQakTx/ktQRETepj/xvHuqHKJzoRzSvQ=='

url = 'http://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList'



# 전운량 : dc10Tca, 시간 : tm, 기온 : ta, 강수량 : rn
# 시작일 : startDt, 시작시 : startHh, 종료시 : endHh, 종료일 : 	endDt


def weather_data(url='http://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList', start_date='20201005', end_date='20211005'):

    cloud_avg_list = []
    temp_avg_list = []
    rain_avg_list = []
    time_list = []
    weather_list = []

    while True:


        params ={'serviceKey' : f'{dekey}', 'numOfRows' : '24', 'pageNo' : '1', 'dataType' : 'JSON', 'dataCd' : 'ASOS', 'dateCd' : 'HR', 'startDt' : f'{start_date}', 'startHh' : '06', 'endDt' : f'{start_date}', 'endHh' : '23', 'stnIds' : '108' }
        response = requests.get(url, params=params)
        a = json.loads(response.text)
        data = a['response']['body']['items']['item']



        cloud_list = []
        temp_list = []
        rain_list = []
        

        for i in data:


            time = i['tm']
            cloud = i['dc10Tca']
            temp = float(i['ta'])
            rain = i['rn']

            if rain == '':

                rain = rain.replace('', '0')
            rain = float(rain)

            if  cloud == '':

                cloud = cloud.replace('', '0')
            cloud = float(cloud)

            cloud_list.append(cloud)
            temp_list.append(temp)
            rain_list.append(rain)
            time = time[0:10]

        cloud_avg = round(sum(cloud_list) / len(cloud_list))
        temp_avg = round(sum(temp_list) / len(temp_list), 1)
        rain_avg = round(sum(rain_list) / len(rain_list), 1)

        if rain_avg != 0:

            weather_list.append('비')

        elif cloud_avg <= 2:

            weather_list.append('맑음')
        
        elif cloud_avg >= 3 and cloud_avg <=5:

            weather_list.append('구름조금')

        elif cloud_avg >= 6 and cloud_avg <= 8:

            weather_list.append('구름많음')
        
        elif cloud_avg <= 10:

            weather_list.append('흐림')

        

        cloud_avg_list.append(cloud_avg)
        temp_avg_list.append(temp_avg)
        rain_avg_list.append(rain_avg)
        time_list.append(time)


        s_d = datetime.strptime(start_date, '%Y%m%d')


        t_d = s_d + timedelta(days=1)

        c = datetime.strftime(t_d, '%Y-%m-%d')
        a = c.split('-')
        h = a[0] + a[1] + a[2]

        start_date = h

        if start_date == end_date:

            break

    return cloud_avg_list, temp_avg_list, rain_avg_list, time_list, weather_list



def weather_dataframe(s_date='20201005', e_date='20211006'):

    cloud_list, temp_list, rain_list, time_list, weather_list = weather_data(url='http://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList', start_date = s_date, end_date = e_date)

    df = pd.DataFrame(data = {'time': time_list, 'temp': temp_list, 'cloud': cloud_list, 'rain': rain_list, 'weather': weather_list})

    return df

weather_df = weather_dataframe(s_date='20210925', e_date='20211005')

#print(weather_df)

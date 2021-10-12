import requests
import json
import pandas as pd
import joblib




def c_weather_df(city='seoul'):

    api_key = '' # openweathermap api key

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=kr'

    res = requests.get(url)
    pre_data = json.loads(res.text)

    a = pre_data['weather']
    c_weather = a[0]['description']
    c_temp = round(pre_data['main']['temp'] - 273.15, 1)
    c_cloud = round(pre_data['clouds']['all'] / 10)
    c_rain = 0

    if c_cloud >= 0 and c_cloud <= 2:

        c_weather = '맑음'

    elif c_cloud >= 3 and c_cloud <= 5:

        c_weather = '구름조금'

    elif c_cloud >= 6 and c_cloud <= 8:

        c_weather = '구름많음'

    else : 

        c_weather = '흐림' 

    if pre_data['weather'][0]['main'] == 'Rain':

        c_rain = round(pre_data['rain']['1h'], 1)
        c_weather = '비'

    data = pd.DataFrame(data = {'temp': c_temp, 'cloud': c_cloud, 'rain': c_rain}, index = [0])

    return data, c_weather, c_temp, c_cloud, c_rain


def predict_genre(c_data):

    joblib_file = 'joblib_model.pkl' 
    model = joblib.load(joblib_file)

    y_pred = int(model.predict(c_data))

    if y_pred == 0:

        y_pred = '가요 / 댄스'

    elif y_pred == 1:

        y_pred = '가요 / 랩/힙합'

    elif y_pred == 2:

        y_pred = '가요 / 발라드'

    elif y_pred == 3:

        y_pred = 'OST / 드라마'

    elif y_pred == 4:

        y_pred = 'POP / 팝'

    else:

        y_pred = '가요 / 락'

    return y_pred

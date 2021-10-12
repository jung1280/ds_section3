from flask import render_template, Blueprint
from openweather import *
from genre_recommend import *
from papago2 import get_translate2

bp1 = Blueprint('base', __name__)

@bp1.route('/')
def base():

    return render_template('main.html')


@bp1.route('/map')
def map():

    state = ['서울', '부산', '대구', '포항', '광주', '전주', '원주', '강릉', '천안']

    c_weather_list = []
    c_temp_list = []
    c_cloud_list = []
    c_rain_list = []
    pred_genre_list = []

    for i in state:

        t_i = get_translate2(i)
        c_data, c_weather, c_temp, c_cloud, c_rain = c_weather_df(t_i)
        pred_genre = predict_genre(c_data)

        c_weather_list.append(c_weather)
        c_temp_list.append(c_temp)
        c_cloud_list.append(c_cloud)
        c_rain_list.append(c_rain)
        pred_genre_list.append(pred_genre)

    return render_template('map.html', state=state, c_weather_list=c_weather_list, c_temp_list=c_temp_list, c_cloud_list=c_cloud_list, c_rain_list=c_rain_list, pred_genre_list=pred_genre_list)


@bp1.route('/map/<project>')
def map_weather(project):


    state = ['서울', '부산', '대구', '포항', '광주', '전주', '원주', '강릉', '천안']

    c_weather_list = []
    c_temp_list = []
    c_cloud_list = []
    c_rain_list = []
    pred_genre_list = []

    for i in state:

        t_i = get_translate2(i)
        c_data, c_weather, c_temp, c_cloud, c_rain = c_weather_df(t_i)
        pred_genre = predict_genre(c_data)

        c_weather_list.append(c_weather)
        c_temp_list.append(c_temp)
        c_cloud_list.append(c_cloud)
        c_rain_list.append(c_rain)
        pred_genre_list.append(pred_genre)

    project_t = get_translate2(project)

    c_data, c_weather, c_temp, c_cloud, c_rain = c_weather_df(project_t)

    pred_genre = predict_genre(c_data)

    title_list, artist_list, album_list = song_recommend(pred_genre)

    num_list = []

    for j in range(0, 20):

        num_list.append(j)

    return render_template('map.html', state=state, c_weather_list=c_weather_list, c_temp_list=c_temp_list, c_cloud_list=c_cloud_list, c_rain_list=c_rain_list, pred_genre_list=pred_genre_list, city=project, c_data=c_data, c_weather=c_weather, c_temp=c_temp, c_cloud=c_cloud, c_rain=c_rain, pred_genre=pred_genre, title_list=title_list, artist_list=artist_list, album_list=album_list, num_list = num_list)    


@bp1.route('/city_search/')
def search_page():


    return render_template('city_search.html')

@bp1.route('/city_search/<project>')
def search_city_page(project):

    project_t = get_translate2(project)

    c_data, c_weather, c_temp, c_cloud, c_rain = c_weather_df(project_t)

    pred_genre = predict_genre(c_data)

    title_list, artist_list, album_list = song_recommend(pred_genre)

    num_list = []

    for i in range(0, 20):

        num_list.append(i)

    return render_template("city_search.html", city=project, c_data=c_data, c_weather=c_weather, c_temp=c_temp, c_cloud=c_cloud, c_rain=c_rain, pred_genre=pred_genre, title_list=title_list, artist_list=artist_list, album_list=album_list, num_list = num_list)



@bp1.route('/<project>')
def project_page(project):

    project_t = get_translate2(project)

    c_data, c_weather, c_temp, c_cloud, c_rain = c_weather_df(project_t)

    pred_genre = predict_genre(c_data)

    title_list, artist_list, album_list = song_recommend(pred_genre)

    num_list = []

    for i in range(0, 20):

        num_list.append(i)

    return render_template("city_search.html", city=project, c_data=c_data, c_weather=c_weather, c_temp=c_temp, c_cloud=c_cloud, c_rain=c_rain, pred_genre=pred_genre, title_list=title_list, artist_list=artist_list, album_list=album_list, num_list = num_list)


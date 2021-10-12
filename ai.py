import pandas as pd
from category_encoders import OrdinalEncoder
from sklearn.model_selection import GridSearchCV
import pandas.io.sql as psql
import psycopg2 as pg
from xgboost import XGBClassifier
import joblib


host = 'chunee.db.elephantsql.com'
user = 'yrcnwtvs'
password = 'PNWvJPSUDXE57B51i4NGHtUzzNUqytLw'
database = 'yrcnwtvs'

target = 'selected_genre'

def dataframe():

    with pg.connect(database=database,
                    password=password,
                    user=user,
                    host=host,
                    port=5432) as conn2:

        sql = 'SELECT * FROM track_weather'
        data = psql.read_sql(sql, conn2)

    return data

def preprocess(df):

    df = df.drop(['weather', 'time'], axis = 1)
    
    map = [{'col': target, 'mapping': {'가요 / 댄스': 0, '가요 / 랩/힙합': 1, '가요 / 발라드': 2, 'OST / 드라마': 3, 'POP / 팝': 4, '가요 / 락': 5}}]
    encode = OrdinalEncoder(cols = target, mapping = map)

    en_df = encode.fit_transform(df)

    X_df = en_df.drop(target, axis = 1)
    y_df = en_df[target]

    return X_df, y_df

df = dataframe()

X_df, y_df = preprocess(df)
total_df = pd.concat([X_df, y_df], axis = 1)


def xgb_grid(df):

    X_df = df.drop(target, axis = 1)
    y_df = df[target]

    xg = XGBClassifier(n_estimators=120, max_depth=5, learning_rate=0.1, random_state=2, n_jobs=-1, objective='multi:softmax')

    dists = {'xgbclassifier__n_esimator' : [100, 110, 120, 130, 200],
          'xgbclassifier__max_depth' : [4, 5, 6, 7, 8],
          'xgbclassifier__learning_rate': [0.1, 0.2, 0.3]}

    grid = GridSearchCV(xg, param_grid = dists, scoring = 'f1', verbose = 1, n_jobs = -1, cv = 5)
    grid.fit(X_df, y_df)

    
    model = grid.best_estimator_


    return model

joblib_file = 'joblib_model.pkl'
joblib.dump(xgb_grid(total_df), joblib_file)







import psycopg2

host = ''
user = ''
password = ''
database = '' # db정보

def create_table():

    conn = psycopg2.connect(host=host
                                , user=user
                                , password=password
                                , database=database)
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS collect')
    cur.execute('CREATE TABLE collect(state VARCHAR(120))')

    conn.commit()

def insert_data(data):

    conn = psycopg2.connect(host=host
                                , user=user
                                , password=password
                                , database=database)
    cur = conn.cursor()
    
    data = (data,)

    cur.execute('INSERT INTO collect(state) VALUES(%s)', data)
    conn.commit()

def export_data():

    conn = psycopg2.connect(host=host
                                , user=user
                                , password=password
                                , database=database)
    cur = conn.cursor()

    cur.execute('SELECT * FROM collect')
    data = cur.fetchone()

    cur.execute('DELETE FROM collect')

    conn.commit()

    return data

#create_table()
data = 'hi'
insert_data(data)

ex_data = export_data()

print(ex_data[0])

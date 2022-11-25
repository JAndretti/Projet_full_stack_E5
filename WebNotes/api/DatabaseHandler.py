import os, time
import psycopg2
import pandas as pd
from sqlalchemy import create_engine


def GetResto(nom):
    qry = f'''SELECT * from resto WHERE nom='{nom}';'''
    cursor.execute(qry)
    return cursor.fetchall()

def GetbyQuartier(quartier):
    qry = f'''SELECT * from resto WHERE quartier='{quartier}';'''
    cursor.execute(qry)
    return cursor.fetchall()

def AddResto(resto):
    qry = f'''\
    INSERT INTO resto (nom, quartier, adresse, ville, coord, type)
    VALUES(%s, %s, %s, %s, %s, %s);'''

    values = (resto.nom, resto.quartier, resto.adresse, 
        resto.ville, resto.coord, resto.type)
    
    cursor.execute(qry, values)
    conn.commit()    

# def DeleteNote(note_id):
#     qry = f'''DELETE FROM notes WHERE note_id='{note_id}';'''
#     cursor.execute(qry)
#     conn.commit()

# def UpdateNote(note):
#     DeleteNote(note.note_id)
#     AddNote(note)

def CreateTable():
    cursor.execute(''' CREATE TABLE IF NOT EXISTS resto(
        nom varchar(1024) NOT NULL PRIMARY KEY,
        quartier varchar(1024) NOT NULL,
        adresse varchar(1024) NOT NULL,
        ville varchar(1024) NOT NULL,
        coord varchar(1024) NOT NULL,
        type varchar(1024) NOT NULL
    ); ''')
    
    conn.commit()



while True:
    try:
        # conn = psycopg2.connect(
        #     host = os.environ['DB_HOST'],
        #     database = os.environ['DB_NAME'],
        #     user = os.environ['DB_USERNAME'],
        #     password = os.environ['DB_PASSWORD']
        # )
        # cursor = conn.cursor()
        host = os.environ['DB_HOST']
        database = os.environ['DB_NAME']
        user = os.environ['DB_USERNAME']
        password = os.environ['DB_PASSWORD']


        conn_string = f"postgresql://{user}:{password}@db/{database}"

        db = create_engine(conn_string)
        conn = db.connect()

        data = pd.read_csv("resto.csv", sep=";")
        max=data.shape[0]-1
        data.columns = ["quartier", "nom", "adresse", "ville", "coord", "type"]
        data = data[[ "nom","quartier", "adresse", "ville", "coord", "type"]]
        data['quartier']=data['quartier'].astype(str)
        data.to_sql("resto", con=conn, if_exists='replace', index=False)


        conn = psycopg2.connect(conn_string)

        conn.autocommit = True
        cursor = conn.cursor()

        sql1 = '''select * from "resto";'''
        cursor.execute(sql1)
        for i in cursor.fetchall():
            print(i)

        print("Database Connected Successfully :-)")
        break
        
    except Exception as error:
        print("Connecting to database failed...Trying Again...")
        print("Error:", error)
        time.sleep(2)





# conn.commit()
# conn.close()

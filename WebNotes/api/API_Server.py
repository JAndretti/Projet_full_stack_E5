import uuid
import os
from ORM import Resto
import DatabaseHandler as db
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
from fastapi import FastAPI

app = FastAPI()

db.CreateTable()
db_cols = [
    'nom', 'quartier', 'adresse', 
    'ville', 'coord', 'type'
]

@app.get('/')
def Home():
    return "Service is Running..."

@app.get('/resto/{nom}')
def resto(nom: str):
    resto = db.GetResto(nom)
    ret = [
        {x:y for (x,y) in zip(db_cols, row)}
        for row in resto
    ]
    return ret

@app.get('/quartier/{quartier}')
def GetbyQuartier(quartier: str):
    quartier = db.GetbyQuartier(quartier)
    ret = [
        {x:y for (x,y) in zip(db_cols, row)}
        for row in quartier
    ]
    print(ret)
    return ret


@app.post('/add_resto')
def AddResto(resto: Resto):
    print("sdkhjbjaehbvjhdfsvbhifadsv",resto)
    resto.nom = str(uuid.uuid4())
    db.AddResto(resto)
    return resto

# @app.get('/delete/{note_id}')
# def DeleteNote(note_id: str):
#     db.DeleteNote(note_id)
#     return 'Deleted '+note_id

# @app.post('/update_note')
# def UpdateNote(note: Note):
#     db.UpdateNote(note)
#     return note


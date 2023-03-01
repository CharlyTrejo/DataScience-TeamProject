from fastapi import FastAPI
from deta import Deta
import pandas as pd

app=FastAPI()
deta = Deta("collections_key")
drive = deta.Drive("migracion")

df_prediccion = pd.read_csv(drive.get('prediccion.csv'))
df_migracion = pd.read_csv(drive.get('df_ml.csv'))

@app.get('/')
def root():
    return "Proyecto grupal migraciones"

@app.get("/prediccion/{country_code}/{anio}")
def prediccion(country_code:str,anio:str):
    return df_prediccion[df_prediccion['codigo_pais'] == country_code][anio].to_list()

@app.get('/codigos')
def codigos():
    dicc = dict(zip(df_migracion['pais_x'],df_migracion['codigo_pais']))
    return dicc

# @app.get("/indicadores/{country_code}/{anio}")
# def indicadores(country_code:str,anio:str):
#     return df_migracion[(df_migracion['codigo_pais'] == country_code) & (df_migracion['anio'] == anio)].to_json(orient='records', force_ascii=False)
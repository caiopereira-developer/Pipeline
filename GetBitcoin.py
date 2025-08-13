import requests
from datetime import datetime
import pandas as pd

def get_bitcoin_df():

    url = "https://api.coinbase.com/v2/prices/spot"

    response = requests.get(url)
    data = response.json()
    
    #quais dados quero em cada instancia
    preco = float(data['data']['amount'])
    ativo = data ['data']['base']
    moeda = data['data']['currency']
    horario = datetime.now()

    #Criação do dataframe 
    df= pd.DataFrame([{
        'ativo' : ativo,
        'preco': preco,
        'moeda': moeda,
        'horario':horario
    }])

    return df


from datetime import datetime
import yfinance as yf

def get_commodities_df():
    ultimo_df = yf.Ticker("GC=F").history(period="1d", interval='1m')[['Close']].tail(1)
    ultimo_df = ultimo_df.rename(columns={"Close": "Preco"})
    ultimo_df['ativo'] = "GC=F"
    ultimo_df['moeda'] = "USD"
    ultimo_df['horario'] = datetime.now()
    ultimo_df = ultimo_df[['ativo', 'moeda', 'horario', 'Preco']]
    return ultimo_df



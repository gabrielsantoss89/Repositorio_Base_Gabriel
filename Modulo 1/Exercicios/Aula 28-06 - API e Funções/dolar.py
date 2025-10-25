import yfinance

def yahoo():
    moeda = "BRL=x"
    dolar = yfinance.Ticker(moeda)

    ultimo = dolar.fast_info['last_price']
    return ultimo

    #print(ultimo) 
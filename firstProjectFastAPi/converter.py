from os import getenv
import requests
import aiohttp #como uma versão async do requests

from fastapi import HTTPException


ALPHAVANTAGEAPIKEY = getenv('API_KEY')

def sync_conveter(from_currency: str, to_currency: str, price: float):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHAVANTAGEAPIKEY}'

    try:
        response = requests.get(url=url)
    except Exception as error:
        raise HTTPException(status_code=400, detail=error)
    
    data = response.json()

    print(data)
    print("\n\n")

    if "Realtime Currency Exchange Rate" not in data:
        raise HTTPException(status_code=400, detail='Realtime Currency Exchange Rate not is in response')
    
    exchange_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

    return price * exchange_rate


async def async_conveter(from_currency: str, to_currency: str, price: float):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHAVANTAGEAPIKEY}'

    try:
       async with aiohttp.ClientSession() as session:
           async with session.get(url=url) as response:
               data = await response.json()
    except Exception as error:
        raise HTTPException(status_code=400, detail=error)
    
    print(data)
    print("\n\n")

    if "Realtime Currency Exchange Rate" not in data:
        raise HTTPException(status_code=400, detail='Realtime Currency Exchange Rate not is in response')
    
    exchange_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

    return price * exchange_rate

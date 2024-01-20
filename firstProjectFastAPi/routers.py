from fastapi import APIRouter
from converter import sync_conveter, async_conveter
from asyncio import gather

router = APIRouter(prefix='/converter')

@router.get('/{from_currency}')
def converter(from_currency: str, to_currencies: str, price: float):
    to_currencies= to_currencies.split(',')

    result = []

    for currency in to_currencies:
        response = sync_conveter(
            from_currency=from_currency,
            to_currency=currency,
            price=price
        )

        result.append(response)


    return result

@router.get('/async/{from_currency}')
async def async_converter(from_currency: str, to_currencies: str, price: float):
    to_currencies= to_currencies.split(',')

    coroutines = []

    for currency in to_currencies:
        coro = async_conveter(
            from_currency=from_currency,
            to_currency=currency,
            price=price
        )

        coroutines.append(coro)

    result = await gather(*coroutines)
    return result
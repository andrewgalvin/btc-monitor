from utils.coin import Coin


def get_price():
    import requests
    headers = {
        "cache-control": "no-cache"
    }
    try:
        response = requests.get(headers=headers, url='https://api.coindesk.com/v1/bpi/currentprice.json')
        data = response.json()
    except:
        raise Exception("Unable to obtain price from CoinDesk."
                        )
    return Coin(
        name=data['chartName'],
        updated=data['time']['updatedISO'],
        price=data['bpi']['USD']['rate']
    )

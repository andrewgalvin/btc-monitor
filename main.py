from utils.scraper import get_price
from firebase import firebase
import time
import json

def post_to_database(c):
    db = firebase.FirebaseApplication("INSERT FIREBASE LINK HERE", None)
    db.put(f'/crypto/coins/btc/{c.updated}', name="updated", data=c.updated)
    db.put(f'/crypto/coins/btc/{c.updated}', name="price", data=c.price)

def write_to_file(c):
    with open('A:\\Big Data\\btc.json', 'a') as f:
        json.dump(c.to_json(), f)
        f.write('\n')


if __name__ == "__main__":
    price = ""
    updated = ""

    while True:
        coin = get_price()
        if coin.price != price:
            price = coin.price
            updated = coin.updated
            write_to_file(coin)
        time.sleep(60)

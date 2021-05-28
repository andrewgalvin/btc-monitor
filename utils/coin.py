class Coin:

    def __init__(self, name, updated, price):
        self.name = name
        self.updated = updated
        self.price = price

    def __str__(self):
        return str({
            "name": self.name,
            "updated": self.updated,
            "price":self.price
        })
from classandfunctions.error_message import error
class Items:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @staticmethod
    def calculate(*args):
        item_prices = 0
        for items in args:
            if items.price == '':
                error()
            else:
                item_prices += int(items.price)

        return item_prices



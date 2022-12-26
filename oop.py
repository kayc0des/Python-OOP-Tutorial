class Item:
    def __init__(self, name: str, price: float, quantity=0):
        """init runs as soon as an object of a class is instantiated."""
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, 5)
print(item1.calculate_total_price())

item2 = Item("Laptop", 1000, 1)
print(item2.calculate_total_price())




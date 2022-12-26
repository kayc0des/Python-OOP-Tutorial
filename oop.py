class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # Run validationns to the received arguments
        assert price >= 0, f"Price {price} is not >= 0!"
        assert quantity >= 0, f"Quantity {quantity} is not >= 0!"
        
        """init runs as soon as an object of a class is instantiated."""
        #assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, 5)

item2 = Item("Laptop", 1000, 1)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

#more attributes could be added to an 
#instance which weren't part of the innit
item2.has_numpad = False




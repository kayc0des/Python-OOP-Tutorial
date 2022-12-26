class Item:
    # Create class attribute
    # Pay rate after 20% discount
    pay_rate = 0.8 

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

    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 1)

item1.apply_discount()
print(item1.price)

#Find out all attributes that belonng ann object
print(Item.__dict__) #class level
print(item1.__dict__) #instance level

print(item1.calculate_total_price())
print(item2.calculate_total_price())

#more attributes could be added to an 
#instance which weren't part of the innit
item2.has_numpad = False




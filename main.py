class Item:

    # Class attribute: Pay rate after 20% discount
    pay_rate = 0.8 

    def __init__(self, name: str, price: float, quantity=0):
        """init runs as soon as an object of a class is instantiated."""
        
        # Run validationns to the received arguments
        assert price >= 0, f"Price {price} is not >= 0!"
        assert quantity >= 0, f"Quantity {quantity} is not >= 0!"
        
        #assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)


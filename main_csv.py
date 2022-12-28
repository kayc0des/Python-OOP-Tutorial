import csv


class Item:
    
    # Class attribute: Pay rate after 20% discount
    pay_rate = 0.8 

    all = []

    def __init__(self, name: str, price: float, quantity=0):
        """init runs as soon as an object of a class is instantiated."""
        
        # Run validationns to the received arguments
        assert price >= 0, f"Price {price} is not >= 0!"
        assert quantity >= 0, f"Quantity {quantity} is not >= 0!"
        
        #assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    #instantitiating from a csv file we need to use a class method
    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    def __repr__(self):
        return f"Item('{self.name}, {self.price}, {self.quantity}')"

Item.instantiate_from_csv()
print(Item.all)


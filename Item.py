class Item:
    def __init__(self, name, price, quantity, people=None):
        if people is None:
            people = []
        self.name = name
        self.price = price
        self.quantity = quantity
        self.people = people

    # equals based on all properties
    def __eq__(self, other):
        return self.name == other.name and self.price == other.price \
               and self.quantity == other.quantity and self.people == other.people

    # get methods
    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getQuantity(self):
        return self.quantity

    def getPeople(self):
        return self.people

    # Modify array of people with item
    def removePerson(self, name):
        self.people.remove(name)

    def insert(self, name):
        self.people.append(name)

    # Set methods
    def setPrice(self, price):
        self.price = price

    def Quantity(self, quantity):
        self.quantity = quantity


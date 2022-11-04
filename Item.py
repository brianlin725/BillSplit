class Item():
    def __init__(self, name, price, unit, people=None):
        if people is None:
            people = []
        self.name = name
        self.price = price
        self.unit = unit
        self.people = people

    # equals based on all properties
    def __eq__(self, other):
        return self.name == other.name and self.price == other.price \
               and self.unit == other.unit and self.people == other.people

    # get methods
    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getUnit(self):
        return self.unit

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

    def setUnit(self, unit):
        self.unit = unit


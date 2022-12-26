class Person:
    def __init__(self, name, items=None):
        if items is None:
            items = []
        self.name = name
        self.items = items

    # Equals based on the name
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name
        return self.name == other

    # return methods
    def getName(self):
        return self.name

    def getItems(self):
        return self.items

    # set methods
    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)

    # Set method
    def setName(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Thing:
    pass

print(Thing)

example = Thing()
print(example)

class Thing2:
    letters = 'abc'
    
print(Thing2.letters)

class Thing3:
    def __init__(self):
        self.letters = 'xyz'
    
something = Thing3()
print(something.letters)

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return f'name={self.name}, symbol={self.symbol}, number={self.number}'

hydrogen = Element('Hydrogen', 'H', 1)

el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(**el_dict)
print(hydrogen)
# クラスのオーバーライド

class Person:
    def __init__(self, name):
        self.name = name
        
class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name
        
class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"
        
person = Person('Tai')
doctor = MDPerson('Tai')
lawyer = JDPerson('Tai')

print(person.name)
print(doctor.name)
print(lawyer.name)
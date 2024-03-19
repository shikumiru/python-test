class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
def print_info(p):
    print('名前', p.name)
    print('年齢', p.age)
        
def age_check(p, i):
    return p.age > i

def print_younger_person_name(p1, p2):
    if p1.age <= p2.age:
        print(p1.name)
    else:
        print(p2.name)
        
def get_total_age(p1, p2):
    return p1.age + p2.age
        
a = Person("東京太郎", 15)
b = Person("埼玉花子", 23)

print_info(a)
print(age_check(a,20))
print_younger_person_name(a, b)
print(get_total_age(a, b))
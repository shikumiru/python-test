import pprint
class PrettyMixin:
    def dump(self):
        pprint.pprint(vars(self))

class Thing(PrettyMixin):
    pass
    
t = Thing()
t.name = "Nyarlathotep"
t.feature = "ichor"
t.age = "eldritch"
t.dump()
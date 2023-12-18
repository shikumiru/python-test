import unicodedata
def unicode_test(value):
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print(f'value="{value}", name="{name}", value2="{value}"')
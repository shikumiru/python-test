def get_odds():
    for number in range(1, 10, 2):
        yield number
        
count = 1
for number in get_odds():
    if count == 3:
        print(number)
        break
    count += 1
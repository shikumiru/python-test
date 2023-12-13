for value in [3, 2, 1, 0]:
    print(value)
    
guess_me = 7
number = 1
while True:
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it')
        break
    else:
        print('opps')
        break
    number += 1
    
guess = 5
for num in range(10):
    if num < guess:
        print("too low")
    elif num == guess:
        print("found it")
        break
    else:
        print("oops")
        break
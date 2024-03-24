def fizzbuzz(number):
    if number % 15 == 0:
        return "FizzBuzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return number
    
if __name__ == "__main__":
    for i in range(1,101):
        print(fizzbuzz(i))
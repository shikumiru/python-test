prime_numbers = []

for num in range(2, 10001):
    is_prime = True
    # 平方根までの間に約数が存在する　かつ　int関数で切り捨てて整数にしエラーを回避
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)
        
print(prime_numbers)
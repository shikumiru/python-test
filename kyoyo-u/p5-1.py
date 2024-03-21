# x の平方根を求める
x = int(input("平方根を求めたい自然数を入力："))

rnew = x

for i in range(10):
    r1 = rnew
    r2 = x/r1
    rnew = (r1 + r2)/2
    
print(r1, rnew, r2)

y = x ** (1/2)
print(y)
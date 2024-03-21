def square_root(x):
    '引数xの平方根を求める'
    rnew = x
    
    diff = rnew - x/rnew
    if diff < 0:
        diff = abs(diff)
    while (diff > 1.0e-6):
        r1 = rnew
        r2 = x/r1
        rnew = (r1 + r2)/2
        print(r1, rnew, r2)
        diff = r1 -r2
        if diff < 0:
            diff = abs(diff)
    return rnew

v = float(input("平方根を求めたい自然数を入力："))
r = square_root(v)
print("結果は", r)
# リストに添え字
a = [5, 1, 3, 4]
for i, d in enumerate(a):
    print(i, d)
    
# リストの要素の平均値
a = [5, 1, 3, 4]
sum = 0
for i in range(len(a)):
    sum += a[i]
average = sum/len(a)
print(average)

a = [i*i for i in range(5)]
print(a)
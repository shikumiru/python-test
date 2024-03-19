total = 0
i = 10
while i < 21:
    total += i
    i += 1
print(total)

total2 = 0
for i in range(10, 21):
    if i == 15:
        continue
    total2 += i
print(total2)
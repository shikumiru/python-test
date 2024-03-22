from turtle import *
# 正 n 角形下の星形
n = 9
for i in range(n):
    forward(100)
    left(180-(180/n))
done()
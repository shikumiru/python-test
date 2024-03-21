# x の平方根を求める
while True:
    x = input("平方根を求めたい自然数を入力：")
    try:
        x = float(x)
    except ValueError:
        print(x, "は数字に変換できません")
        continue
    except:
        print("予期せぬエラー")
        exit()
    if x <=0:
        print(x, "は正の数値ではありません")
        continue
    
    print("平方根を求める数値：", x)
    break

rnew = x

diff = rnew - x/rnew
if diff < 0:
    diff = -diff
while (diff > 1.0e-6):
    r1 = rnew
    r2 = x/r1
    rnew = (r1 + r2)/2
    print(r1, rnew, r2)
    diff = r1 - r2
    if diff < 0:
        diff = -diff
        
# 無限ループ型
rnew = x

while True:
    r1 = rnew
    r2 = x/r1
    rnew = (r1 + r2)/2
    print(r1, rnew, r2)
    diff = r1 - r2
    if diff < 0:
        diff = -diff
    if diff <= 1.0e-6:
        break
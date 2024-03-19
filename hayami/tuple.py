t = (0, 1, 4, 9, 16, 25, 36, 49)
print(t)
print(type(t))

# リストと同じようにアクセス
print(t[0])
print(t[-1])
print(t[::-1])
# リストと同じように要素の確認
print(16 in t)
print(16 not in t)
# 要素の変更・追加は不可

# 作成するときの括弧を省略できる
t = 2, 4, 6
print(t)
print(type(t))
# タプルの各要素の値を取り出しながら代入（アンパック）
x, y, z = t
print(x)
print(y)
print(z)
# 要素数が合わないとアンパックできない
# x, y = t
# x, y, z, a = t
x, y, z = 1, 3, 5
print(x)
print(y)
print(z)
# 一時変数を使うことなく、変数の値の交換できる、タプルのパックとアンパックによる動作
print(x, y, z, 7)
y, z, x = x, y, z
print(x, y, z)
# 関数が複数の値を返すことができるのは、関数の戻り値がタプルに変換されるから
def fg(x):
    return x ** 2 -2, 2 * x
r = fg(1)
print(r)
fx, gx = r
print(fx)
print(gx)
# リストから要素をアンパックすることもできる
a = [0, 2, 4]
x, y, z = a
print(x)
print(y)
print(z)

# 特殊なタプル
# 一つの要素からなるタプルを作成するには、末尾にカンマを付ける
t = (1,)
print(t)
# 空のタプル作成はtuple関数を用いる
t = tuple()
print(t)

# リストとタプルの相互変換
a = [1, 3, 5]
print(type(a))
b = tuple(a)
print(b)
print(type(b))
c = list(b)
print(c)
print(type(c))
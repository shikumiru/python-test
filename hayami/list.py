a = [0, 1, 4, 9, 16, 25, 36, 49]
print(type(a))

# 先頭要素のインデックス番号は0
print(a[0])
print(a[1])
# リストの要素数 len関数
print(len(a))
# リストの最後の要素のインデックス番号　要素数 -1
print(a[len(a)-1])
# リストの要素を末尾からアクセスするために、負のインデックス番号を用いれる
print(a[-2])

# 空のリスト作成
b = []
b = list()

# スライス
print(a[2:5]) # 開始位置と終了位置
print(a[:3]) # 開始位置を省略
print(a[5:]) # 終了位置を省略
print(a[-3:]) # 負のインデックス番号の利用
print(a[1::2]) # 要素を取り出す間隔を指定
print(a[5:2:-1]) # 逆順に要素を取り出す
print(a[::-1]) # 開始・終了位置を省略し、すべての要素を逆順

# リストの要素に対する繰り返し
for x in a:
    print(x)    
# 各要素のインデックス番号を得る
for i, x in enumerate(a):
    print(i, x, a[i])
# リストの要素の末尾から繰り返しアクセス
for x in reversed(a):
    print(x)

# リストの要素に対する操作
wd = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
print(wd)
# リスト内の要素を変更
wd[1] = 'tue'
print(wd)
# 末尾に要素を追加
wd.append('saturday')
print(wd)
# 指定した要素を削除
del wd[5]
print(wd)
# リストを連結し、新しいリストを作成
d = wd + ['saturday', 'sunday']
print(d)
# 末尾の要素を取り出し、同時にリストから削除
d.pop()
print(d)
# push操作に相当するappend関数
d.append('sun')
print(d)

# 要素の並べ替え 降順に並べる
print(sorted(d))
# 元のリストは変更されていない
print(d)
# 引数reverseをTrueにセットし、昇順に並べる
print(sorted(d, reverse=True))
# 要素の長さを取得する無名関数（lambda）を定義し、それをkey引数に渡して、文字数の少ない順に並び替え
print(sorted(d, key=lambda x: len(x)))
# reverseと併用して多い順
print(sorted(d, key=lambda x: len(x), reverse=True))
# 要素を降順に並び替え　リスト内の要素が並び替えられる
d.sort()
print(d)
# 要素を昇順に並び替え
d.sort(reverse=True)
print(d)
# 引数keyに関数を指定し、要素の並べ方を変更
d.sort(key=lambda x: len(x))
print(d)

# 要素の所属検査
print('sun' in d)
print('sun' not in d)

# リストと参照
x = ['mon', 'tue', 'wed', 'thu', 'fri']
print(x)
y = x
print(y)
# yに要素を追加
y.append('sat')
y.append('sun')
print(y)
# xの要素も変更されている
print(x)

# リストのコピー
l = ['mon', 'tue', 'wed', 'thu', 'fri']
print(l)
m = l[:]
m.append('sat')
m.append('sun')
print(m)
# この場合リストlの要素は変更されてない
print(l)

# リストと関数の引数
# 引数で与えられたリストの末尾に'END'を追加するappend_endを定義
def append_end(s):
    s.append('END')
t = ['one', 'two']
print(t)
append_end(t)
print(t)

# リストの様々な作成方法
c = list(range(10))
print(c)
c = list(range(1, 10, 2))
print(c)
# リストの要素はデータ型が異なってても可
e = [1, 'one', 'first']
print(e[0])
print(e[1])

# リストの内包表記
a2 = []
for i in range(10):
    a2.append(i * 2)
print(a2)
# 内包表記で簡潔に書ける
a2n = [i * 2 for i in range(10)]
print(a2n)
print([i * 3 for i in range(10)])
# 内包表記を入れ子にして、掛算表を2次元配列として作成
import pprint
m = [[i * j for i in range(10)] for j in range(10)]
pprint.pprint(m)
print(m[2])
print(m[2][3])

f = [[0 for i in range(10)] for j in range(10)]
pprint.pprint(f)
f[3][5] = 2
pprint.pprint(f)
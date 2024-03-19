s = 'stress'
print(s)
print(type(s))
print(len(s))

# 空文字列の作成
s = ''
s = str()

# エスケープ・シーケンス
s1 = 'C:\\Users\\okazaki'
print(s1)
s2 = r'C:\Users\okazaki'
print(s2)

t1 = "stress's"
print(t1)
t2 = "stress\'s"

# 複数行
s = """先頭行
2行目
3行目"""
print(s)

# 数値と文字列の変換
x = 10
s = str(x) #str関数
print(s)

s = '10'
x = int(s) #int関数
print(x)

s = '3.14'
x = float(s) #float関数
print(x)

print(bin(255)) # 2進数形式の文字列への変換
print(hex(255)) # 16進数形式の文字列への変換

# インデックス
s = 'stressed'
print(s[0])
print(s[len(s)-1])
print(s[-1])
print(s[-3])
# スライス
print(s[0:3])
print(s[:3])
print(s[6:])
print(s[:-2])
print(s[-2:])
print(s[:6:2])
print(s[::2])
print(s[::-1])

# 文字列に対する操作
s = "https://www.nlp.c.titech.ac.jp/search?q=Natural+Language+Processing"
print(s.lower()) # 小文字へ変換
print(s.upper()) # 大文字へ変換
print(s.replace('a', 'b')) # 置換
print(s.find('/')) # 文字列が最初に現れるインデックスを返す
print(s.find('html')) # 見つからない場合は-1を返す
print(s.rfind('/')) # 指定した文字列が最後に現れるインデックスを返す
# 指定した文字で文字列を分割し、リストで表現する
v = s[40:].split('+')
print(v)
# 指定した文字で連結する
t = ','.join(v)
print(t)
# 先頭or末尾に指定した文字が付いているとき、取り除く
s = '  one, two, three,'
print(s.strip(' '))
print(s.strip(', '))
# 末尾に指定した文字が付いているとき、取り除く
print(s.rstrip(','))
# 先頭に指定した文字が付いているとき、取り除く
print(s.lstrip(' '))

# 文字列に対する条件
s = "Tokyo Institute of Technology 2020"
print(s == 'ToykoTech')
print(s != 'TokyoTech')
print(s <'Tokyo Tech')
print(s > 'Tokyo Tech')
print('Tokyo' in s)
print('University' not in s)
print(s.startswith('Tokyo'))
print(s.endswith('Technology'))
print(s.isupper())
print(s[0].isupper())
print(s.islower())
print(s[1].islower())
print(s.isspace())
print(s.isalpha())
print(s.isnumeric())
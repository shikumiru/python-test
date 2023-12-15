palindrome = 'A man,\nA plan,\nA canal:\nPanama.'
print(palindrome)

# スライス

letters = 'abcdefghijklmnopqrstuvwxyz'
# 全体
print(letters[:])
# 21字以降
print(letters[20:])
# 11字以降
print(letters[10:])
# 13~15字
print(letters[12:15])
# 末尾から3文字
print(letters[-3:])
# 18字目から末尾4字目まで
print(letters[18:-3])
# 末尾から6字目を先頭として、末尾から3字目まで
print(letters[-6:-2])
# 先頭から末尾まで7字ごとに切り出す
print(letters[::7])
# 4から19まで、3文字ごと
print(letters[4:20:3])
# 19から末尾まで4文字ごと
print(letters[19::4])
# 先頭からオフセット20まで5文字ごと
print(letters[:21:5])
# 逆順
print(letters[::-1])

# 文字列の長さ所得
print(len(letters))
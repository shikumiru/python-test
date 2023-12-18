import itertools

# 引数全体を１つのように扱い、要素を反復する
for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)
    
# 引数を循環的に無限に返す
# for itemb in itertools.cycle([1, 2]):
    # print(itemb)
    
# 要素を計算していく
for itemc in itertools.accumulate([1, 2, 3, 4]):
    print(itemc)
    
# 第2引数として関数を受け付ける
def multiply(a, b):
    return a * b

for itemd in itertools.accumulate([1, 2, 3, 4], multiply):
    print(itemd)
## 独学プログラマー 
## 21章 データ構造 P.257

# ▼▼ チャレンジ 1 ▼▼
class Stack:
    def __init__(self):
        self.items = []

    # スタックが空かの確認
    def is_empty(self):
        return not self.items

    # スタック最に要素を追加
    def push(self, item):
        self.items.append(item)

    # スタック最後の要素を削除し、返す
    def pop(self):
        return self.items.pop()

    # スタック最後の要素を取得
    def peek(self):
        return self.items[-1]
    
    # スタックサイズを取得
    def size(self):
        return len(self.items)

# エントリポイント
stack = Stack()

for c in "yesterday":
    stack.push(c)

reversed_string = ""

print(" ** Before ** ")
print("stack.items：" + str(stack.items))
print("reversed_string：" + reversed_string)
while stack.size():
    reversed_string += stack.pop()

print("\n ** After ** ")
print("stack.items：" + str(stack.items))
print("reversed_string：" + reversed_string)
# ▲▲ チャレンジ 1 ▲▲

""" ▼▼ 出力結果 ▼▼

 ** Before ** 
stack.items：['y', 'e', 's', 't', 'e', 'r', 'd', 'a', 'y']
reversed_string：

 ** After ** 
stack.items：[]
reversed_string：yadretsey

    ▲▲ 出力結果 ▲▲ """

# ▼▼ チャレンジ 2 ▼▼
class Stack:
    def __init__(self):
        self.items = []

    # スタックが空かの確認
    def is_empty(self):
        return not self.items

    # スタック最に要素を追加
    def push(self, item):
        self.items.append(item)

    # スタック最後の要素を削除し、返す
    def pop(self):
        return self.items.pop()

    # スタック最後の要素を取得
    def peek(self):
        return self.items[-1]
    
    # スタックサイズを取得
    def size(self):
        return len(self.items)

# エントリポイント
stack = Stack()

cha2List = [1, 2, 3, 4, 5]
revcha2List = []

for c in cha2List:
    stack.push(c)

print(" ** Before ** ")
print("stack.items：" + str(stack.items))
print("cha2List：" + str(cha2List))
print("revcha2List：" + str(revcha2List))

while stack.size():
    revcha2List.append(stack.pop())

print("\n ** After ** ")
print("stack.items：" + str(stack.items))
print("cha2List：" + str(cha2List))       # リスト
print("revcha2List：" + str(revcha2List)) # 要素逆順の新リスト

# ▲▲ チャレンジ 2 ▲▲
""" ▼▼ 出力結果 ▼▼

 ** Before ** 
stack.items：[1, 2, 3, 4, 5]
cha2List：[1, 2, 3, 4, 5]
revcha2List：[]

 ** After ** 
stack.items：[]
cha2List：[1, 2, 3, 4, 5]
revcha2List：[5, 4, 3, 2, 1]

    ▲▲ 出力結果 ▲▲ """
# 解答URL：https://github.com/calthoff/tstp/tree/master/part_IV/data_structures/challenges

## 独学プログラマー 
## 21章 データ構造 P.251～252

# ▼▼ スタックについて ▼▼
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

for c in "Hello":
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

# ▲▲ スタックについて ▲▲

""" ▼▼ 出力結果 ▼▼

 ** Before ** 
stack.items：['H', 'e', 'l', 'l', 'o']
reversed_string：

 ** After ** 
stack.items：[]
reversed_string：olleH

    ▲▲ 出力結果 ▲▲ """

# 解答URL：https://github.com/calthoff/self_taught/blob/master/python_ex299.py/

## 独学プログラマー
## 12章 プログラミングパラダイム P.156,157

#▼▼ チャレンジ1 ▼▼
class Apple:
    def __init__(self, c, s, w, t):
        self.color = c  # "red", "green"...
        self.size = s   # "small", "big"...
        self.weight = w # 300[g], 400[g]...
        self.taste = t  # "terible", "good"...
#▲▲ チャレンジ1 ▲▲
        
#▼▼ チャレンジ2 ▼▼
import math
class Circle:
    def __init__(self, halfd):
        self.harfd = halfd  # "red", "green"...
        self.farea = 0

    def area(self):
        self.farea = self.harfd * self.harfd * math.pi
        return self.farea

# エントリポイント
cir1 = Circle(10)
print("円の面積 == ")
print(cir1.area())
print(cir1.farea)
print(cir1.harfd)
#▲▲ チャレンジ2 ▲▲

# 解答URL：<http://tinyurl.com/gpqe62e>

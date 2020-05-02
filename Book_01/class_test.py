## 独学プログラマー
## P.156 チャレンジ1
##  りんごの4つの属性を考える。
class Apple:
    def __init__(self, c, s, w, t):
        self.color = c  # "red", "green"...
        self.size = s   # "small", "big"...
        self.weight = w # 300[g], 400[g]...
        self.taste = t  # "terible", "good"...

## P.156 チャレンジ2
##  円の面積を求めるメソッドを作成し、使う。
import math

class Circle:
    def __init__(self, halfd):
        self.harfd = halfd  # "red", "green"...
        self.farea = 0

    def area(self):
        self.farea = self.harfd * self.harfd * math.pi
        return self.farea

## エントリポイント
cir1 = Circle(10)
print("円の面積 == ")
print(cir1.area())
print(cir1.farea)
print(cir1.harfd)

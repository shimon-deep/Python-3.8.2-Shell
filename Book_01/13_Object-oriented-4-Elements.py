## 独学プログラマー 
## 13章 オブジェクト指向プログラミングの4大要素 P.169

#▼▼ チャレンジ1 ▼▼
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.shape = "Rectangle"

    # 外周の長さを返す
    def calculate_perimeter(self):
        return (self.width * 2 + self.length * 2)

class Square:
    def __init__(self, width):
        self.width = width
        self.shape = "Square"

    # 外周の長さを返す
    def calculate_perimeter(self):
        return (self.width * 4)

# エントリポイント
rec = Rectangle(10,30)
squ = Square(15)

shapes = [rec, squ]

for a_shape in shapes:
    print("{}の外周の長さは...".format(a_shape.shape))
    print(a_shape.calculate_perimeter())
#▲▲ チャレンジ1 ▲▲

#▼▼ チャレンジ2 ▼▼
class Square:
    def __init__(self, width):
        self.width = width
        self.shape = "Square"

    # 外周の長さを返す
    def calculate_perimeter(self):
        return (self.width * 4)

    # 横幅を変更する
    def change_size(self, delta):
        self.width += delta

# エントリポイント
squ = Square(15)
print("初期状態の{}の外周の長さは...".format(squ.shape))
print(squ.calculate_perimeter())
try:
    delta = int(input("幅変更\n"))
    squ.change_size(delta)
except ValueError as e:
    print(e.args)
    print("入力した値が不正のため幅変更は行いません。\n")

print("変更後の{}の外周の長さは...".format(squ.shape))
print(squ.calculate_perimeter())

#▲▲ チャレンジ2 ▲▲

#▼▼ チャレンジ3 ▼▼
class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a shape.")
        
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.shape = "Rectangle"

    # 外周の長さを返す
    def calculate_perimeter(self):
        return (self.width * 2 + self.height * 2)

class Square(Shape):
    def __init__(self, width):
        self.width = width
        self.shape = "Square"

    # 外周の長さを返す
    def calculate_perimeter(self):
        return (self.width * 4)

    # 横幅を変更する
    def change_size(self, delta):
        self.width += delta

# エントリポイント
rec = Rectangle(10,30)
squ = Square(15)

rec.what_am_i()
squ.what_am_i()

#▲▲ チャレンジ3 ▲▲

#▼▼ チャレンジ4 ▼▼
class Horse:
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

class Rider:
    def __init__(self, name):
        self.name = name

# エントリポイント
the_rider = Rider("Satoru Suzuki")
hor = Horse("Serturu Naliya", the_rider)

print("{0}(馬)の騎手は{1}です。".format(hor.name, hor.rider.name))

#▲▲ チャレンジ4 ▲▲

# 解答URL：http://tinyurl.com/hz9qdh3

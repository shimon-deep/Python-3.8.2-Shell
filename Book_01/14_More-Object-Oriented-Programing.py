## 独学プログラマー 
## 14章 もっとオブジェクト指向プログラミング P.177

#▼▼ チャレンジ1 ▼▼
class Shape:
    def what_am_i(self):
        print("I am a shape.")
        
class Square(Shape):
    square_list = [] # クラス変数を宣言
    
    def __init__(self, width):
        self.width = width
        self.square_list.append(self)

    def what_am_i(self):
        print("I am a Square.")
      
# エントリポイント
squ1 = Square(15)
print(Square.square_list) # [<__main__.Square object at 0x000001A58202AA60>]
squ2 = Square(20)
print(Square.square_list)
# [<__main__.Square object at 0x000001A58202AA60>, <__main__.Square object at 0x000001A58202AC40>]
    
#▲▲ チャレンジ1 ▲▲

#▼▼ チャレンジ2 ▼▼
class Square:
    def __init__(self, width):
        self.width = width

    def __repr__(self):
        #return (str(self.width) + " by ") * 4
        return ("{} by ".format(self.width)) * 4

# エントリポイント
squ = Square(29)
print(squ) # {29 by 29 by 29 by 29 by}

#▲▲ チャレンジ2 ▲▲

#▼▼ チャレンジ3 ▼▼
class Square():
    def __init__(self, width):
        self.width = width

# オブジェクトの比較結果を返す。
def compare_obj(obj1, obj2):
    return (obj1 is obj2)

# エントリポイント
squ = Square(10)
same_squ = squ
another_squ = Square(10)
print(compare_obj(squ, same_squ))    # {True}
print(compare_obj(squ, another_squ)) # {False}

#▲▲ チャレンジ3 ▲▲

# 解答URL：http://tinyurl.com/j9qjnep

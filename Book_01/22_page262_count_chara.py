## 独学プログラマー 
## 22章 アルゴリズム P.262

# ▼▼ 出現する文字列を数える ▼▼

from collections import Counter

def count_characters(string):
    count_dict = {}
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    print(count_dict)


reserchStr = "Dynasty"
count_characters(reserchStr)
print(Counter(reserchStr))
# ▲▲ 出現する文字列を数える ▲▲

""" ▼▼ 出力結果 ▼▼

{'D': 1, 'y': 2, 'n': 1, 'a': 1, 's': 1, 't': 1}

    ▲▲ 出力結果 ▲▲ """

# 解答URL：https://github.com/calthoff/self_taught/blob/master/python_ex309.py/


def bottles_of_beer(bob):
    """ Prints 99 Bottle 
        of Beer on the
        Wall lyrics.
        :param bob: Must
        be a positive 
        integer.
    """
    if bob < 1:
        print("""No more 
                 bottles 
                 of beer 
                 on the wall. 
                 No more 
                 bottles of 
                 beer.""")
        return
    tmp = bob
    bob -= 1
    print("""{} bottles of 
             beer on the 
             wall. {} bottles
             of beer. Take one 
             down, pass it 
             around, {} bottles 
             of beer on the 
             wall.
          """.format(tmp, 
                     tmp, 
                     bob))
    bottles_of_beer(bob)


bottles_of_beer(99)

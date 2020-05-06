## 独学プログラマー 
## 21章 データ構造 P.255～256
## ** チケット行列 **

# ▼▼ キューについて ▼▼
import time
import random

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def simulate_line(till_show, max_time):
    pq = Queue()
    tix_sold = []

    for i in range(10):
        pq.enqueue("person" + str(i))

        t_end = time.time() + till_show
        now = time.time()

    while now < t_end and not pq.is_empty():
        now = time.time()
        r = random.randint(0, max_time)
        time.sleep(r)
        person = pq.dequeue()
        
        print(person)
        
        tix_sold.append(person)
        
    return tix_sold

# エントリポイント
sold = simulate_line(5, 1)
print(sold)

# ▲▲ キューについて ▲▲

""" ▼▼ 出力結果 ▼▼

person0
person1
person2
person3
person4
person5
person6
['person0', 'person1', 'person2', 'person3', 'person4', 'person5', 'person6']

    ▲▲ 出力結果 ▲▲ """

# 解答URL：https://github.com/calthoff/self_taught/blob/master/python_ex304.py

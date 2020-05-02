## リスト, タプル, 辞書 の使い方テスト ##

ny = {
    "座標":(1, 11.1),

    "事実":{
        "州":"ニューヨーク",
        "国":"アメリカ"
        }
    }

print(ny["事実"]["州"])
print(ny["事実"]["国"])
print(ny["座標"])
print(ny["座標"][0])
print("{0}   {1}".format(12, "arigatou"))

#strWhen = input("いつ？\n")
#str = "入力された日付は {} です。".format( strWhen )
#print(str)

testDic = {
    "dic1":1,
    "dic2":"dicValue2",
    "dic3":"dicValue3",
    }

for i, new in enumerate(testDic):
    print(testDic[new])

tv = ["arii","arii","arii"]

for i, new in enumerate(tv):
    tv[i] = new.upper()

print(tv)

## csvモジュール, ファイルの入出力テスト ##
import csv
import os

with open("st.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["one", "Two", "Three"])
print(os.getcwd())

## printテスト p.145,146 ##
pop = ["a","n"]
jpop = []

# 以下同じ出力結果
print("pop song : {}".format(pop))
print("pop song :", pop)

print("pop song :".join(pop[0] + pop[1]))

## insert ##
List = list()
List.append("a")
List.append("c")
print(List)
List.insert(1,"b")
print(List)

## 独学プログラマー 
## 15章 知識を1つにまとめる P.178～187

from random import shuffle           # カードシャッフル用
from operator import attrgetter      # 順位ソート用

class WarGame:

    def __init__(self):
        self.roundCount = 0          # ラウンドカウンタ初期化
        self.c_deck = Deck()         # デッククラスのインスタンス作成
        self.c_print =Print()        # 出力クラスのインスタンス作成
        self.c_deck.mk_random_deck() # ランダムデック作成
        
    # ルール説明
    def rule_description(self):
        print("""
******************** ルール説明 **********************
1. 各プレイヤーは、トランプの山札から一枚カードを引く。
2. 引いたカードを場に出す。
3. 一番大きい数字を出したプレイヤーの勝利。
******************************************************
              """)

    # エントリープレイヤー決定
    def entry_player(self):
        playerCount = 0              # プレイヤーカウンタ
        self.playerList = []         # プレイヤーリスト
        while True:
            playerCount += 1
            msg = "プレイヤー{0}の名前を入力してください\n"
            name = input(msg.format(playerCount))              # プレイヤー名を入力
            self.playerList.append(Player(name))               # プレイヤーをリストに追加
            self.playerList[playerCount - 1].num = playerCount # プレイヤー番号を格納
            print("")
            
            if playerCount > 1:
                print("※ 他にエントリーする人はいますか？")
                if quit() == "q":
                    break
                
        print("以下プレイヤーがエントリーされています")
        self.c_print._break()
        for i, a_player in enumerate(self.playerList):
            print("プレイヤー{}：".format(i + 1) + a_player.name)
        self.c_print._break()

    # カードをデックから引く
    def draw_card(self):
        self.roundCount += 1
        msg = "****** ラウンド{} ******"
        input(msg.format(self.roundCount))

        for a_player in self.playerList:
            msg = "\n{}さんが、カードを引く番です\n[Enter...]"
            input(msg.format(a_player.name))
            a_player.card = self.c_deck.draw_card()

    # カードオープン
    def open_card(self):
        msg = "\n** カードをオープン **\n[Enter...]"
        input(msg)
        self.c_print._break()
        for a_player in self.playerList:
            msg = "{}さん：{}"
            print(msg.format(
                a_player.name, a_player.card))
        self.c_print._break()
        msg = "[Enter...]"
        input(msg)

    # 勝負
    def match_card(self):
        tmpCard = None
        tmpName = ""
        playerNum = 0 # プレイヤーリストのインデックスを格納

        # 一番強いカードを持つプレイヤーを見つける
        for i, a_player in enumerate(self.playerList):
            if tmpCard is None:
                tmpCard = a_player.card
                playerNum = i
            else:
                if tmpCard < a_player.card:
                    tmpCard = a_player.card
                    playerNum = i
        msg = "\nラウンド{}の勝者は「{}」を引いた\nプレイヤー{}の「{}」さんです！"
        print(msg.format(
            self.roundCount, self.playerList[playerNum].card,
            self.playerList[playerNum].num, self.playerList[playerNum].name))
        self.playerList[playerNum].wins += 1 # 勝利数をカウント
        
    # 順位表示 (wins, num, name)
    def disp_rank(self):
        rank = 1     # 表示順位を格納
        tempWins = 0 # 比較する勝利数を格納

        # 勝利数を基にプレイヤーを降順でソート
        rankList = sorted(
            self.playerList, key = attrgetter('wins'), reverse = True) 
        print("\n順位は...")

        for a_player in rankList:
            # 同順位を考慮して表示順位を算出
            if tempWins == 0:
                tempWins = a_player.wins
            if tempWins > a_player.wins:
                tempWins = a_player.wins
                rank += 1
            msg = "{}位：{}勝 プレイヤー{} {}さん"
            print(msg.format(
                rank, a_player.wins, a_player.num, a_player.name))
            
    # プレイゲーム
    def play_game(self):        
        print("War Game を始めます。")
        self.rule_description()
        self.entry_player()
        
        while len(self.c_deck.deck) >= len(self.playerList):
            if quit() == "q":
                break
            self.draw_card()
            self.open_card()
            self.match_card()

        if len(self.c_deck.deck) < len(self.playerList):
            print("\nデックにカードが残っていないため、優勝者を決定します。")

        self.who_is_winner()
        self.disp_rank()
        if quit() != "q":
            self.roundCount = 0          # ラウンドカウンタ初期化
            self.c_deck.mk_random_deck() # ランダムデック作成
            self.play_game()
        else:
            print("\nまた遊んでね～～")

    # 優勝者決定
    def who_is_winner(self):
        tempWins = 0      # ラウンド勝利数を格納
        winnnersList = [] # 同率優勝者を格納
        tmpName = ""      # 仮優勝者名を格納

        for a_player in self.playerList:
            if tempWins < a_player.wins:
                tempWins = a_player.wins
                winnnersList = []             # 優勝者リストを初期化
                winnnersList.append(a_player) # 優勝者リストにプレイヤーを追加
                
            elif tempWins == a_player.wins:
                winnnersList.append(a_player) # 優勝者リストに同率プレイヤーを追加

        print("\n今回の優勝者は...")
        for a_winner in winnnersList:
            msg = " {}勝した プレイヤー{}の「{}」さん"
            print(msg.format(
                a_winner.wins, a_winner.num, a_winner.name))
        print("です！ おめでとうございます！")
                
class Player:
    
    def __init__(self, name):
        self.name = name # プレイヤー名を格納
        self.wins = 0    # 勝利数を格納
        self.card = None # Cardオブジェクトのため、Noneで初期化
        self.num = 0     # プレイヤー番号を格納

class Deck:

    def __init__(self):
        self.deck = []   # カードリストを宣言

    def mk_random_deck(self):
        for i in range(4):
            for j in range(2, 15):
                self.deck.append(Card(i, j))
        shuffle(self.deck)

    def draw_card(self):
        if len(self.deck) == 0:
            return
        else:
            return self.deck.pop()
        
class Card:

    markList = ["clubs", "diamonds", "hearts", "spades"]

    # Noneを0,1に使うことで、引数値に対応
    valueList = [None, None,
                "2", "3", "4", "5", "6", "7", "8", "9", "10",
                "Jack", "Queen", "King", "Ace"]
    
    def __init__(self, mark, value):
        self.mark = mark   # トランプのマークインデックスを格納
        self.value = value # トランプの値インデックスを格納

    # 特殊メソッド <演算子
    def __lt__(self, otherCard):
        if self.value < otherCard.value:
            return True
        elif self.value == otherCard.value:
            return self.mark < otherCard.mark
        else:
            return False

    # 特殊メソッド >演算子    
    def __gt__(self, otherCard):
        if self.value > otherCard.value:
            return True
        elif self.value == otherCard.value:
            return self.mark > otherCard.mark
        else:
            return False

    # 特殊メソッド print
    def __repr__(self):
        newPrint = self.valueList[self.value] + \
                   " of " + self.markList[self.mark]
        return newPrint

class Print:
    def __init__(self):
        self.symbolNum = 25
        
    def _break(self):
        print("*" * self.symbolNum)

def quit():
    msg = "'q'で終了、それ以外のキーで続行..."
    return input(msg)

# エントリポイント
game = WarGame()
game.play_game()

"""
【補足説明】
変数名について
 mk：make
 rm：remove

▼▼出力結果▼▼
======== RESTART: C:/workspace/Python-3.8.2-Shell/Book_01/15_War_Game.py =======
War Game を始めます。

******************** ルール説明 **********************
1. 各プレイヤーは、トランプの山札から一枚カードを引く。
2. 引いたカードを場に出す。
3. 一番大きい数字を出したプレイヤーの勝利。
******************************************************
              
プレイヤー1の名前を入力してください
suzuki

プレイヤー2の名前を入力してください
satoru

※ 他にエントリーする人はいますか？
'q'で終了、それ以外のキーで続行...
プレイヤー3の名前を入力してください
Strong

※ 他にエントリーする人はいますか？
'q'で終了、それ以外のキーで続行...
プレイヤー4の名前を入力してください
Weak

※ 他にエントリーする人はいますか？
'q'で終了、それ以外のキーで続行...q
以下プレイヤーがエントリーされています
*************************
プレイヤー1：suzuki
プレイヤー2：satoru
プレイヤー3：Strong
プレイヤー4：Weak
*************************
'q'で終了、それ以外のキーで続行...
****** ラウンド1 ******

suzukiさんが、カードを引く番です
[Enter...]

satoruさんが、カードを引く番です
[Enter...]

Strongさんが、カードを引く番です
[Enter...]

Weakさんが、カードを引く番です
[Enter...]

** カードをオープン **
[Enter...]
*************************
suzukiさん：7 of spades
satoruさん：2 of diamonds
Strongさん：10 of diamonds
Weakさん：4 of diamonds
*************************
[Enter...]

ラウンド1の勝者は「10 of diamonds」を引いた
プレイヤー3の「Strong」さんです！
'q'で終了、それ以外のキーで続行...
～～～～
～～～～
ラウンド4の勝者は「10 of spades」を引いた
プレイヤー2の「satoru」さんです！
'q'で終了、それ以外のキーで続行...q

今回の優勝者は...
 2勝した プレイヤー2の「satoru」さん
です！ おめでとうございます！

順位は...
1位：2勝 プレイヤー2 satoruさん
2位：1勝 プレイヤー1 suzukiさん
2位：1勝 プレイヤー3 Strongさん
3位：0勝 プレイヤー4 Weakさん
'q'で終了、それ以外のキーで続行...

また遊んでね～～
▲▲出力結果▲▲
"""
# 解答：本書 P.178～187 参照

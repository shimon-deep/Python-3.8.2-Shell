## 独学プログラマー
## 10章 知識を1つにまとめる P.134～139

def main():
    isPlayGame = True
    print("「Hangmanゲーム」 START")
    print("-----------------------")
    while True:
        strGameWord = input("[Player1]\n1～10文字以内の英単語を入力してください。\n 例)cat\n")
        iGameWordLen = len(strGameWord)

        if (iGameWordLen < 1) or (iGameWordLen > 10):
            print(msg("文字数が不正です。"))
            continue

        hangman(strGameWord)
        msg = "もう一度やる？？ y/n\n"
        isYes = input(msg)
        if isYes == "y":
            continue
        else:
            print("また遊んでね～～")
            break

def hangman(strPlayer1Word):
    isWin = False
    iMissCount = 0
    iSuccCount = 0
    hangList = [
        "     A     ",
        "    A AA   ",
        "   A   AA  ",
        "  AAAAAAAA ",
        " A       AA"
        ]
    
    strTempWord = list("_" * len(strPlayer1Word))
    player1WordList = list(strPlayer1Word)
    
    while iMissCount < len(hangList):
        msg = "\n[Player2]\n1文字予想しよう。\n 例)c\n"
        strPlayer2Word = input(msg)
        print("----------")
        if strPlayer2Word in player1WordList:
            print("\n入力文字が当たった！")
            iSuccCount = iSuccCount + 1
            iIndexCha = player1WordList.index(strPlayer2Word)
            strTempWord[iIndexCha] = strPlayer2Word
            player1WordList[iIndexCha] = "@"
            
        else:
            iMissCount = iMissCount + 1

        print("予想英単語：" + "".join(strTempWord))
        print("\n絵：")
        print("\n".join(hangList[0:iMissCount]))

        if "_" not in strTempWord:
            isWin = True
            break

    if not isWin:
        print("絵(A)が完成しました!")
        print("Player1の勝利です! ")
        print("正解は...{}でした".format(strPlayer1Word))
    else:
        print("英単語を当てました!")
        print("Player2の勝利です!")

    print("...")
    print("「Hangmanゲーム」 FINISH")

def msg(msgNumber):
    msgList = {
        "1":"「Hangmanゲーム」 START",
        "2":"1～10文字以内の英単語を入力してください。\n 例)cat\n",
        "3":"文字数が不正です。",
        "4":"Do you want to quit ?? y/n (y:yes, n:no)",
        "wait":"Please wait...\n"
    }
    return msgList[msgNumber]

# エントリポイント
main()

# 解答URL：http://tinyurl.com/j7rb8or

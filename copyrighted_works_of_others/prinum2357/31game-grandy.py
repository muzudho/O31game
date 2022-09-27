# Author: prinum2357
# Arrangement: Muzudho

def main():
    """グランディ数を返す"""

    # 取っていい石の数（複数）
    s = input("s?(カンマ区切り)").split(",")
    s = [int(s) for s in s]
    # 選択肢の数
    s_len = len(s)

    # 石の数
    n = int(input("n?"))

    # 残りの石の数に対応する各グランディ数
    grandy = [0] * n

    #print("0, 0q")

    # i は残りの石の数
    for i in range(1, n):
        # 局面，　初期値：取っていい石の数のリスト
        g = list(range(i+1))

        # j は、取る石の数
        for j in s:
            # 取る石の数は、残っている石の数を上限とする
            if i-j >= 0:

                # 取る石の数より大きな数は、取り除く
                if grandy[i-j] in g:
                    g.remove(grandy[i-j])

        #print(i, g)

        # 最小の非負整数
        grandy[i] = min(g)

    print(grandy)


if __name__ == "__main__":
    main()

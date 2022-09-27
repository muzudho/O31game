# Author: prinum2357


def main():
    s = input("s?(カンマ区切り)").split(",")
    s = [int(s) for s in s]
    s_len = len(s)

    # 石の数
    n = int(input("n?"))

    grandy = [0] * n

    #print("0, 0q")

    for i in range(1, n):
        # 局面
        g = list(range(i+1))

        for j in s:
            if i-j >= 0:

                # 存在する整数を取り除く
                if grandy[i-j] in g:
                    g.remove(grandy[i-j])

        #print(i, g)

        # 最小の非負整数
        grandy[i] = min(g)

    print(grandy)


if __name__ == "__main__":
    main()

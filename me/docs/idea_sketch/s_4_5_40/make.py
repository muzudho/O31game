"""
cd me/docs/idea_sketch/s_4_5_40

python.exe make.py
"""

print("Idea sketch")


def print_idea_sketch(a, b, c):
    """アイデアスケッチを表示"""

    len_N = c
    scale = len_N / (a * b)  # 定数倍を想定しているが……実数のままにしたろ
    overview_width = int(scale * a)
    overview_height = int(scale * b)

    # 願望を表示
    print(f"""
        This is a wish. I wish it was like this
        =======================================

        S = {{ a, b, c }}
        len(N) = c        scale = c / ab

                        +b
        0 ─────────> b ─────────> 2b         × (a * scale)
                    /           /
                   / -1        /
                  /           /
                a ────────> ★ a+b <---- I guess this is the period.

                × (b * scale)
    """)

    # 当てはめてみる
    print(f"""
        In this case
        ============

        S = {{ {a}, {b}, {c} }}
        len(N) = {c}        scale = {scale}

                        +{b:2}
        0 ─────────>{b:2} ─────────>{2*b:2}         × {overview_width}
                    /           /
                   / -1        /
                  /           /
               {a:2} ────────> ★ {a+b} <---- I guess this is the period.

                × {overview_height}
    """)

    # S は サブトラクションセット

    def print_x_axis():
        """x軸描画"""

        for i in range(-overview_height, len_N+1):
            # 負数の剰余の実装は２種類あるが、Pythonでは上手く行った
            n = i % len_N
            print(f"{n:2}", end="")

        print("\n")

    print_x_axis()

    for y in range(0, overview_height+1):

        indent = ""
        for i in range(0, overview_height-y):
            indent += "  "

        print(indent, end="")

        for x in range(0, overview_width+1):
            # y軸値に横幅を掛けたり、なんかひねくれた式だが、プリントアウトして納得してほしい
            n = (y * a) + ((x-y) * b)
            n %= len_N

            # 間隔
            interval_space = ""
            for i in range(0, a+1):
                # ２桁だと想定しておく
                interval_space += "  "

            print(f"{n:2.0f}{interval_space}", end="")

        print("\n")

    print("")


if __name__ == "__main__":

    #a = 4
    #b = 5
    #c = 2 * a * b
    #print_idea_sketch(a=a, b=b, c=c)
    """S = { a, b, c } を入れてください。
    ただし、 c は ab の定数倍を入れてください。
    レイアウトが崩れないように、 a, b は 50 未満ぐらいの非負整数を選んでください

    とりあえず S = { 4, 5, 40 } を叩き台に選んで、式を作成した。
    """

    enter = input("""S={a,b,c}.
Please input "a b c". However,
    c = ax
    c = by
    x = bz
    y = az
    z = your favorite integer greater than 1
Example:
S=4 5 40
> S=""")
    tokens = enter.split()
    print_idea_sketch(a=int(tokens[0]), b=int(tokens[1]), c=int(tokens[2]))

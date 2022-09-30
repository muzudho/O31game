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
    delta_a_b = a - b  # 負数になる

    # 周期を当てるのに使う
    a_p_c = a + c   # ▲a+c
    a_p_b = a + b   # ■a+b
    b_p_c = b + c   # ●b+c

    # 願望を表示
    print(f"""
        This is a wish. I wish it was like this
        =======================================

        S = {{ a, b, c }}
        len(N) = c        scale = c / ab
        I guess one of ■a+b, ●b+c, ▲a+c is the period.

                  b or b+c
                       ===
        0 ─────────> ● ─────────> 2b         × (a * scale)
                    /    +b     /
                   / a-b       /
                  /           /
                 ▲ ────────> ■ a+b
              a or a+c         ===
                   ===

              × (b * scale)
    """)

    # 当てはめてみる
    print(f"""
        In this case
        ============

        S = {{ {a}, {b}, {c} }}
        len(N) = {c}        scale = {scale}
        I guess one of ■{a_p_b}, ●{b_p_c}, ▲{a_p_c} is the period.

                  {b:2} or {b_p_c:2}
                        ==
        0 ─────────> ● ─────────>{2*b:2}         × {overview_width}
                    /   +{b:2}    /
                   / {delta_a_b}        /
                  /           /
                 ▲ ────────> ■ {a_p_b:2}
              {a:2} or {a_p_c:2}         ==
                    ==

              × {overview_height}
    """)

    # S は サブトラクションセット

    def print_x_axis():
        """x軸描画"""

        for i in range(-overview_height, len_N+1):
            # 負数の剰余の実装は２種類あるが、Pythonでは上手く行った
            n = i % len_N
            print(f"{n:2}", end="")

        print("")  # 改行

        # 下線も引いたろ
        for i in range(-overview_height, len_N+1):
            print(f"──", end="")

        print("")  # 改行

    print_x_axis()

    for y in range(0, overview_height+1):

        indent = ""
        for i in range(0, overview_height-y):
            indent += "  "

        print(indent, end="")

        for x in range(0, overview_width+1):  # 横がループしてることを表したいので 1 多めに
            # y軸値に横幅を掛けたり、なんかひねくれた式だが、プリントアウトして納得してほしい
            n = (y * a) + ((x-y) * b)
            n %= len_N

            # 間隔
            interval_space = ""
            for i in range(0, b-1):
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
    """このアルゴリズムの生まれ方（ぬか喜びの歴史）

    S = { 4, 5, ? } という適当な数を選んだ。

    0-----5
     \\
      \\
       4

    まで想像し、あとは 繰り返せばメッシュができるし、それは路線図のダイアグラムのようでもある。
    まぐれで ベクトルの足し算をしたところ（a+b）に 周期 があった。

    これは特殊な例で、少し数を変えてみると合わなかった。よくある　**ぬか喜び**　だ。
    口惜しいので (mod c) まで OK と考えてみた。そう遠くもない気がした。
    そこで
    ずるをして (a+b) or (b+c) or (a+c) もありにした。

    すると、当てはまるケースが増えた。
    こりゃいいや、と思ったところで、ひとまず、ここまでとする。
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
    S=5 6 60
    S=5 7 105
    S=4 6 72
    S=4 6 48
> S=""")
    tokens = enter.split()
    print_idea_sketch(a=int(tokens[0]), b=int(tokens[1]), c=int(tokens[2]))

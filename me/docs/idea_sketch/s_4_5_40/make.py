"""
cd me

python.exe -m docs.idea_sketch.s_4_5_40.make
"""
from kernel.math.grundy import GrundyListObj

print("This is an idea sketch.")


def print_idea_sketch(a, b, c):
    """アイデアスケッチを表示"""

    scale = c / (a * b)  # 定数倍を想定しているが……実数のままにしたろ
    overview_width = int(scale * a)
    delta_a_b = a - b  # 負数になる

    # 周期を当てるのに使う
    c_p_a = c + a   # ▲c+a
    a_p_b = a + b   # ■a+b
    b_p_c = b + c   # ●b+c

    # 願望を表示
    print(f"""
        This is a wish. I wish it was like this
        =======================================

        S = {{ a, b, c }}    (a < b < c. c = abn)
        c is maximum game size "len(N)"
        I guess one of ■a+b, ●b+c, ▲c+a is the period.
            - ■a+b is just like a constant.
            - ●b+c is mysterious. I have seen it when a<=n<=b, abn=c.
            - ▲c+a when c is a multiple of 3 is often periodic.


                  b is b+c (mod c)
                       ===
        0 ─────────> ● ─────────> 2b
                    /     b     /
                   / a-b       /
                  /           /
                 ▲ ────────> ■ a+b
                               ===
              a is c+a (mod c)
                   ===
    """)

    if a <= scale and scale <= b:
        is_this_a_n_b = " "
    else:
        is_this_a_n_b = "not "

    # 当てはめてみる
    print(f"""
        In this case
        ============

        S = {{ {a}, {b}, {c} }}    ({a} < {b} < {c}. {c} = {a}・{b}n)
        n = {scale}. n is scale.        This is {is_this_a_n_b}a <= n <= b.
        I guess one of ■{a_p_b}, ●{b_p_c}, ▲{c_p_a} is the period.

                  {b:2} is {b_p_c:2} (mod {c})
                        ==
        0 ─────────> ● ─────────>{2*b:2}
                    /    {b:2}     /
                   / {delta_a_b}        /
                  /           /
                 ▲ ────────> ■ {a_p_b:2}
                               ==
              {a:2} is {c_p_a:2} (mod {c})
                    ==
    """)

    # S は サブトラクションセット

    x_axis_zero_len = 1
    x_axis_positive_len = 2*c
    """描画するx軸の０を含む整数部の長さ。平行四辺形を描きたいので、２週している"""

    x_axis_negative_len = c // a + 1
    """x軸の負数をどこまで描画すればいいかというと、 a の距離で c に届くまで。ループを見たいので、左端を1多く取る"""

    is_display_negative_parallelogram = True
    """X軸の負数部に伸びる平行四辺形を描くか？"""

    display_c = c
    """表示する正味の部分のX方向の長さ"""

    y_axis_height = 2*c // a + 1
    """y軸をどこまで描画すればいいかというと、a の距離で c に届くまで。ループを見たいので、左端を1多く取る"""

    if (a == 1 and b == 4 and c == 20):
        """X軸の負数部にめっちゃ伸びるやつは個別対応"""
        # TODO 調整むずかしいから、すっきりさせたい
        x_axis_negative_len = 5*c
        x_axis_positive_len = 5*c
        overview_width *= 3
        display_c = 3*c
        y_axis_height = 3*c // a + 1
    elif (a == 1 and b == 4 and c % 20 == 0) or (a == 3 and b == 7 and c == 42) or (a == 3 and b == 9 and c == 27):
        """X軸の負数部が巨大になる想定外のケースは個別に対応。X軸の負数部を表示しないことにする"""
        x_axis_positive_len = 3*c
        x_axis_negative_len = 0
        is_display_negative_parallelogram = False
        overview_width *= 2
        display_c = 2*c
    else:
        pass

    delta_y = b - a
    """ナナメに y軸 の並びを見たときの間隔"""

    # グランディ数を表示するのに使う
    grundy_list_obj = GrundyListObj.make(
        S={a, b, c}, len_N=x_axis_negative_len+display_c)

    x_axis_width = x_axis_negative_len + x_axis_zero_len + x_axis_positive_len
    """描画するx軸全体の長さ"""

    minimum_x = c - x_axis_negative_len
    """描画する最小のx"""

    # x軸の間隔
    x_axis_interval_space = ""
    for _ in range(0, b-1):
        # ２桁だと想定しておく
        x_axis_interval_space += "  "

    def print_x_axis():
        """x軸描画"""
        for x in range(minimum_x, minimum_x+x_axis_width):
            # 負数の剰余の実装は２種類あるが、Pythonでは上手く行った
            n = x % c
            print(f"{n:2}", end="")

        print(" for vector coordinates")  # 改行

    def print_x_axis_reversing_for_the_game():
        """x軸描画
        X軸は 右から左に読む（反転している）ことに注意"""

        display_length = x_axis_negative_len + display_c + 1

        # 目盛り
        for x in range(0, display_length):
            rev_x = display_length - x - 1
            rev_x %= 100  # 2桁しか表示できない
            print(f"{rev_x:2}", end="")

        # スペース パディング
        indent = ""
        for _ in range(0, c):
            indent += "  "

        print(indent, end="")

        print(" reversing for the game")  # 改行

    def print_x_axis_bit_grundy():
        """グランディ数の描画
        X軸は 右から左に読む（反転している）ことに注意"""

        display_length = x_axis_negative_len + display_c + 1

        # 目盛り
        for i in range(0, display_length):
            rev_x = display_length - i - 1
            grundy = grundy_list_obj.get_bit_grundy_at(rev_x)
            print(f"{grundy:2}", end="")

        # スペース パディング
        indent = ""
        for _ in range(0, c):
            indent += "  "

        print(f"{indent} bit-grundy (right to left)")  # 改行

    def print_underline_x_axis():
        """下線も引いたろ"""
        for _ in range(minimum_x, minimum_x+x_axis_width):
            print(f"──", end="")

        print("")  # 改行

    def print_table():
        """表の描画"""

        y_end = y_axis_height // 2 + 1

        for y in range(0, y_end):  # 末尾と先頭がループしていることを見せたいので、 +1 広め
            """上半分の台形（X軸の負数部を描かないのであれば平行四辺形）の部分"""

            padding_width = x_axis_negative_len - y * delta_y

            # ドット パディング
            indent = ""
            for _ in range(0, padding_width):
                indent += " ."

            print(indent, end="")

            if is_display_negative_parallelogram:
                """X軸の負数部も描くのであれば、台形にする"""
                for x in range(0, overview_width+1+y):  # yが１段下がるほど、xは右に1伸びる。台形になる
                    # y軸値に横幅を掛けたり、なんかひねくれた式だが、プリントアウトして納得してほしい
                    n = (y * a) + ((x-y) * b)
                    n %= c

                    print(f"{n:2.0f}{x_axis_interval_space}", end="")
            else:
                padding_width = x_axis_negative_len + y * a

                # ドット パディング
                indent = ""
                for x in range(0, padding_width):
                    indent += " ."

                print(indent, end="")

                # 正味の部分
                for x in range(0, overview_width+1):  # x軸方向の幅は変わらない
                    n = (a*y + b*x) % c
                    print(f"{n:2.0f}{x_axis_interval_space}", end="")

            print("\n")  # 空行をはさむ

        if is_display_negative_parallelogram:
            """X軸の負数部を描いた場合、平行四辺形を伸ばさないと形が悪くなるので伸ばす"""

            for y in range(y_end, y_axis_height):
                """下半分の平行四辺形の部分"""
                padding_width = x_axis_negative_len + y * a

                # ドット パディング
                indent = ""
                for x in range(0, padding_width):
                    indent += " ."

                print(indent, end="")

                for x in range(0, overview_width+1):  # x軸方向の幅は変わらない
                    n = (a*y + b*x) % c
                    print(f"{n:2.0f}{x_axis_interval_space}", end="")

                print("\n")  # 空行をはさむ

        print("\n")

    print_x_axis_bit_grundy()
    print_underline_x_axis()
    print_x_axis_reversing_for_the_game()
    print_underline_x_axis()
    print_x_axis()
    print_underline_x_axis()
    print_table()


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
    ずるをして (a+b) or (b+c) or (c+a) もありにした。

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
    S=4 5 40    S=2 3 12                                         S=1 3 15    S=1 4 20
    S=4 5 20    S=2 4 16   S=5 6 60     S=4 6 48    S=1 3 9      S=3 9 27
    S=4 5 60    S=2 5 10   S=5 7 105    S=4 6 72    S=1 3 15     S=3 7 42
> S=""")
    tokens = enter.split()
    print_idea_sketch(a=int(tokens[0]), b=int(tokens[1]), c=int(tokens[2]))

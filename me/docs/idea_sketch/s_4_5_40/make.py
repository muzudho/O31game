"""
cd me/docs/idea_sketch/s_4_5_40

python.exe make.py
"""

print("Idea sketch")


def print_idea_sketch(a, b):
    """アイデアスケッチを表示"""

    magic_number = 2
    overview_width = magic_number * a
    overview_height = magic_number * b
    len_N = 2 * a * b
    width_scale = len_N / overview_width  # 縦幅で割ると横幅が出てくる（ひねくれていることに注意）
    height_scale = len_N / overview_height
    print(f"\nlen_N:{len_N} overview_height:{overview_height} overview_width:{overview_width} width_scale:{width_scale:2.1f} height_scale:{height_scale:2.1f}\n")

    # 願望を表示
    print(f"""
        This is a wish. I wish it was like this.
        ========================================

        S = {{ a, b, 2ab }}

                        b
        0 ─────────> b ─────────> 2b         × {overview_width}
                    /           /
                   / a         /
                  /           /
                a ────────> ★ a+b <---- I guess this is the period.

                × {overview_height}
    """)

    # 当てはめてみる
    print(f"""
        In this case
        ============

        S = {{ {height_scale:2.1f}, {width_scale:2.1f}, {len_N} }}

                        {width_scale:2.1f}
        0 ─────────>{b:2} ─────────>{2*b:2}         × {overview_width}
                    /           /
                   / {height_scale:2.1f}       /
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
            # なんかひねくれた式だが、プリントアウトして納得してほしい
            n = (y * height_scale) + ((x-y) * width_scale)
            n %= len_N
            # TODO ここのスペース要修正
            print(f"{n:2.0f}        ", end="")

        print("\n")

    print("")


if __name__ == "__main__":

    print_idea_sketch(a=4, b=5)
    """S = { a, b, c } ただし、 c は自動的に決まるので a, b だけを入れてください。
    レイアウトが崩れないように、 a, b は 50 未満ぐらいの数を選んでください

    とりあえず S = { 4, 5, 40 } を叩き台に選んで、式を作成した。
    """

"""
cd me/docs/idea_sketch/s_4_5_40

python.exe make.py
"""

print("Idea sketch")

len_N = 40
overview_width = 8
overview_height = 10
width_scale = len_N / overview_width  # 縦幅で割ると横幅が出てくる（ひねくれていることに注意）
height_scale = len_N / overview_height
print(f"\nlen_N:{len_N} overview_height:{overview_height} overview_width:{overview_width} width_scale:{width_scale:2.1f} height_scale:{height_scale:2.1f}\n")

# サブトラクションセット
print(f"S={{ {height_scale:2.1f}, {width_scale:2.1f}, {len_N} }}")

print(f"""
            {width_scale:2.1f}
       0──────────> × {overview_width}
       /\\          \\
   -1 /  \ {height_scale:2.1f}      \\
     /    \\          \\
            ─────────>★ <---- I guess this is the period.
    × {overview_height}
""")


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

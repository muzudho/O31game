"""
cd me/docs/idea_sketch/s_4_5_40

python.exe make.py
"""

print("Idea sketch")

len_N = 40
overview_width = 10
overview_height = 8
width_scale = len_N / overview_height  # 縦幅で割ると横幅が出てくる（ひねくれていることに注意）
height_scale = len_N / overview_width
print(f"\nlen_N:{len_N} overview_width:{overview_width} overview_height:{overview_height} width_scale:{width_scale:2.1f} height_scale:{height_scale:2.1f}\n")

print(f"""
            {width_scale:2.1f}
        ──────────> × {overview_height}
       /\\
   -1 /  \ {height_scale:2.1f}
     /    \\
    × {overview_width}
""")

for y in range(0, overview_width+1):

    indent = ""
    for i in range(0, overview_height-y+2):
        indent += "  "

    print(indent, end="")

    for x in range(0, overview_width-1):
        # なんかひねくれた式だが、プリントアウトして納得してほしい
        n = (y * height_scale) + ((x-y) * width_scale)
        n %= len_N
        print(f"{n:2.0f}      ", end="")

    print("\n")

print("")

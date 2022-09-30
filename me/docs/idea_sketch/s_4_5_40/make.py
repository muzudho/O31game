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
print(f"\nlen_N:{len_N} overview_width:{overview_width} overview_height:{overview_height} width_scale:{width_scale} height_scale:{height_scale}\n")

print(f"""
  {width_scale:2.0f}
──────> × {overview_width}
\\
 \ {height_scale:2.0f}
  \\
    × {overview_height}
""")

for y in range(1, overview_height+1):

    indent = ""
    for i in range(0, y):
        indent += "  "

    print(indent, end="")

    for x in range(0, overview_width):
        n = x * height_scale + y
        print(f"{n:2.0f}      ", end="")

    print("\n")

print("")

"""
cd me

python.exe -m drawing.main
"""
import cv2
import numpy as np
from datetime import datetime

a = 1
b = 2
c = 3
len_Nz = 40
zoom = 0.5

# 描画する画像を作る,128を変えると色を変えれます 0黒→255白
image_width = 1200
canvas = np.full((250, image_width, 3), 240, dtype=np.uint8)
font_color = (55, 55, 55)

# 線、描画する画像を指定、座標1点目、2点目、色、線の太さ
#line_color = (55, 55, 55)
#cv2.line(canvas, (120, 10), (220, 110), line_color, thickness=1)


# サブトラクションセットを表示
cv2.putText(canvas,
            f"S = {{ {a}, {b}, {c} }}",
            (int(5*zoom), int(30*zoom)),  # x,y
            None,  # font
            1.0 * zoom,  # font_scale
            font_color,  # color
            0)  # line_type

# とりあえず c の２倍はある要素数

Nz = [0] * (len_Nz+1)

# 盤
board = [""] * len_Nz

# 駒の配置の算出
for i in range(1, len_Nz):
    dst_a = i-a
    dst_b = i-b
    dst_c = i-c
    if 0 < dst_a:
        if board[dst_a] == "":
            board[i] += "a"

    if 0 < dst_b:
        if board[dst_b] == "":
            board[i] += "b"

    if 0 < dst_c:
        if board[dst_c] == "":
            board[i] += "c"

for i in range(1, len_Nz):
    if board[i] == "":
        board[i] = "."

# 駒を描画
for i in range(0, len_Nz):
    cv2.putText(canvas,
                f"{board[i]}",
                (int((i*50+5)*zoom), int(90*zoom)),  # x,y
                None,  # font
                1.0 * zoom,  # font_scale
                font_color,  # color
                0)  # line_type

# x軸を描画
for i in range(0, len_Nz):
    cv2.putText(canvas,
                f"{i}",
                (int((i*50+5)*zoom), int(150*zoom)),  # x,y
                None,  # font
                1.0 * zoom,  # font_scale
                font_color,  # color
                0)  # line_type


date = datetime.now().strftime("%Y%m%d_%H%M%S")
cv2.imwrite(f"./output/{date}_tmp.png", canvas)

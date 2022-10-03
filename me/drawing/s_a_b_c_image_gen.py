import cv2
import numpy as np
# from datetime import datetime


def gen_s_a_b_c_image(a, b, c, len_Nz, zoom=1.0):
    """
    Parameters
    ----------
    zoom : float
        描画倍率
    """

    margin_left = 5

    char_width = 50
    """一文字の幅の目安"""

    image_width = int((len_Nz * char_width + margin_left) * zoom)
    image_height = int(char_width*10*zoom)

    # 描画する画像を作る,128を変えると色を変えれます 0黒→255白
    canvas = np.full((image_height, image_width, 3), 240, dtype=np.uint8)
    font_color = (55, 55, 55)
    line_color = (55, 55, 55)
    line_thickness = 1

    # サブトラクションセットを表示
    cv2.putText(canvas,
                f"S = {{ {a}, {b}, {c} }}",
                (int(5*zoom), int(30*zoom)),  # x,y
                None,  # font
                1.0 * zoom,  # font_scale
                font_color,  # color
                0)  # line_type

    board = [""] * len_Nz
    """盤"""

    mate_lines = []
    """mate線"""

    # 駒の配置 と mate線 の算出
    for i in range(0, len_Nz):
        dst_a = i-a
        dst_b = i-b
        dst_c = i-c
        if 0 <= dst_a:
            if board[dst_a] == "":
                board[i] += "a"
                mate_lines.append(("a", i, dst_a))

        if 0 <= dst_b:
            if board[dst_b] == "":
                board[i] += "b"
                mate_lines.append(("b", i, dst_b))

        if 0 <= dst_c:
            if board[dst_c] == "":
                board[i] += "c"
                mate_lines.append(("c", i, dst_c))

    for i in range(0, len_Nz):
        if board[i] == "":
            board[i] = "."

    def print_pieces(y):
        """駒を描画"""
        for i in range(0, len_Nz):
            cv2.putText(canvas,
                        f"{board[i]}",
                        (int((i*char_width+margin_left)*zoom), y),  # x,y
                        None,  # font
                        1.0 * zoom,  # font_scale
                        font_color,  # color
                        0)  # line_type

    def print_occupied_pieces(y):
        """駒の有無を描画"""
        for i in range(0, len_Nz):
            if board[i] == ".":
                piece = "x"
            else:
                piece = "."

            cv2.putText(canvas,
                        f"{piece}",
                        (int((i*char_width+margin_left)*zoom), y),  # x,y
                        None,  # font
                        1.0 * zoom,  # font_scale
                        font_color,  # color
                        0)  # line_type

    def print_x_axis(y):
        """x軸を描画"""
        for i in range(0, len_Nz):
            cv2.putText(canvas,
                        f"{i}",
                        (int((i*char_width+margin_left)*zoom), y),  # x,y
                        None,  # font
                        1.0 * zoom,  # font_scale
                        font_color,  # color
                        0)  # line_type

    def print_mate_lins(src_y, dst_y):
        """mate線を描画"""
        for mate_line in mate_lines:
            # 線、描画する画像を指定、座標1点目、2点目、色、線の太さ
            src_i = mate_line[1]
            src_x = int((char_width*src_i+margin_left)*zoom)

            dst_i = mate_line[2]
            dst_x = int((char_width*dst_i+margin_left)*zoom)

            cv2.line(canvas, (src_x, src_y),
                     (dst_x, dst_y), line_color, thickness=line_thickness)

    print_pieces(y=int(90*zoom))
    """駒を描画"""

    print_mate_lins(src_y=int(110*zoom), dst_y=int(380*zoom))
    """mate線を描画"""

    print_occupied_pieces(y=int(400*zoom))
    """駒の有無を描画"""

    print_x_axis(y=int(440*zoom))
    """x軸を描画"""

    # date = datetime.now().strftime("%Y%m%d_%H%M%S")
    cv2.imwrite(f"./output/s_{a}_{b}_{c}_tmp.png", canvas)

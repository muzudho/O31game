import cv2
import numpy as np
# from datetime import datetime
from kernel.math.grundy import GrundySequence


def gen_s_a_b_c_image(a, b, c, len_Nz, zoom=1.0, suffix=""):
    """
    Parameters
    ----------
    zoom : float
        描画倍率
    """

    margin_left = 5

    char_width = 50
    char_height = 40
    """一文字の幅の目安"""

    grundy_sequence = GrundySequence.make(S={a, b, c}, len_N=len_Nz-1)
    """グランディ数列"""

    image_width = int((len_Nz * char_width + margin_left) * zoom)
    image_width = int(image_width/2)  # 全体を入れるのではなく、左半分ぐらいを画像にする
    image_height = int(char_height*13*zoom)

    # 描画する画像を作る,128を変えると色を変えれます 0黒→255白
    canvas = np.full((image_height, image_width, 3), 240, dtype=np.uint8)
    # Blue,Green,Red
    font_color = (55, 55, 55)
    color_red = (90, 90, 220)
    color_green = (90, 220, 90)
    color_blue = (220, 90, 90)
    line_thickness = 1

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

    def print_subtraction_set(y):
        """サブトラクションセットを表示"""
        cv2.putText(canvas,
                    f"S = {{ {a}, {b}, {c} }}",
                    (int(5*zoom), int(y*zoom)),  # x,y
                    None,  # font
                    1.0 * zoom,  # font_scale
                    font_color,  # color
                    0)  # line_type

    def print_empty_pieces(y):
        """駒を描画"""
        for i in range(0, len_Nz):
            if board[i] == ".":
                cv2.putText(canvas,
                            f".",
                            (int((i*char_width+margin_left)*zoom), int(y*zoom)),  # x,y
                            None,  # font
                            1.0 * zoom,  # font_scale
                            font_color,  # color
                            0)  # line_type

    def print_a_pieces(y):
        """駒を描画"""
        for i in range(0, len_Nz):
            if "a" in board[i]:
                cv2.putText(canvas,
                            f"a",
                            (int((i*char_width+margin_left)*zoom),
                             int(y*zoom)),  # x,y
                            None,  # font
                            1.0 * zoom,  # font_scale
                            color_red,  # color
                            0)  # line_type

    def print_b_pieces(y):
        """駒を描画"""
        for i in range(0, len_Nz):
            if "b" in board[i]:
                cv2.putText(canvas,
                            f"b",
                            (int((i*char_width+margin_left)*zoom), int(y*zoom)),  # x,y
                            None,  # font
                            1.0 * zoom,  # font_scale
                            color_green,  # color
                            0)  # line_type

    def print_c_pieces(y):
        """駒を描画"""
        for i in range(0, len_Nz):
            if "c" in board[i]:
                cv2.putText(canvas,
                            f"c",
                            (int((i*char_width+margin_left)*zoom), int(y*zoom)),  # x,y
                            None,  # font
                            1.0 * zoom,  # font_scale
                            color_blue,  # color
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
                        (int((i*char_width+margin_left)*zoom), int(y*zoom)),  # x,y
                        None,  # font
                        1.0 * zoom,  # font_scale
                        font_color,  # color
                        0)  # line_type

    def print_x_axis(y):
        """x軸を描画"""
        for i in range(0, len_Nz):
            cv2.putText(canvas,
                        f"{i}",
                        (int((i*char_width+margin_left)*zoom), int(y*zoom)),  # x,y
                        None,  # font
                        1.0 * zoom,  # font_scale
                        font_color,  # color
                        0)  # line_type

    def print_grundy_sequence(y):
        """グランディ数列を図形的に描画"""
        for i in range(0, len_Nz):
            grundy_number = grundy_sequence.get_grundy_at(i)

            if grundy_number == 0:
                label = "x"
                vertical_repeat = 1
            else:
                label = "."
                vertical_repeat = grundy_number

            for j in range(0, vertical_repeat):  # 文字を上にずらしながら重ねていく
                cv2.putText(canvas,
                            label,
                            (int((i*char_width+margin_left)*zoom),
                             int((y-(char_height/4)*j)*zoom)),  # x,y
                            None,  # font
                            1.0 * zoom,  # font_scale
                            font_color,  # color
                            0)  # line_type

    def print_mate_lins(src_y, dst_y):
        """mate線を描画"""
        for mate_line in mate_lines:
            # 線、描画する画像を指定、座標1点目、2点目、色、線の太さ
            s_element = mate_line[0]
            if s_element == "a":
                line_color = color_red
            elif s_element == "b":
                line_color = color_green
            elif s_element == "c":
                line_color = color_blue

            src_i = mate_line[1]
            src_x = int((char_width*src_i+margin_left)*zoom)

            dst_i = mate_line[2]
            dst_x = int((char_width*dst_i+margin_left)*zoom)

            cv2.line(canvas, (src_x, int(src_y*zoom)),
                     (dst_x, int(dst_y*zoom)), line_color, thickness=line_thickness)

    y = 0
    y += 30
    print_subtraction_set(y=y)
    """サブトラクションセットを表示"""

    y += 50  # 80
    print_c_pieces(y=y)
    """駒を描画"""

    y += char_height  # 120
    print_b_pieces(y=y)
    """駒を描画"""

    y += char_height  # 160
    print_a_pieces(y=y)
    """駒を描画"""

    print_empty_pieces(y=y)
    """重ねてエンプティ駒を描画"""

    y += 20  # 180, 450
    print_mate_lins(src_y=y, dst_y=y+270)
    """mate線を描画"""

    y += 290  # 470
    print_grundy_sequence(y=y)

    y += char_height  # 530
    print_x_axis(y=y)
    """x軸を描画"""

    # date = datetime.now().strftime("%Y%m%d_%H%M%S")
    cv2.imwrite(f"./output/s_{a:02}_{b:02}_{c:02}{suffix}_tmp.png", canvas)

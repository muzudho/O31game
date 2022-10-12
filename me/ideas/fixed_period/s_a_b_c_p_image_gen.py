import cv2
import numpy as np
# from datetime import datetime
from kernel.math.grundy_sequence import GrundySequence


def gen_s_a_b_c_p_image(S: set, p, zoom=1.0, suffix="", is_temporary=True):
    """
    Parameters
    ----------
    zoom : float
        描画倍率
    """

    # 昇順ソート a < b < c
    S_list = list(S)
    S_list.sort()
    a = S_list[0]
    b = S_list[1]
    c = S_list[2]

    stone_symbolds = ["a", "b", "c"]
    """石の表示"""

    len_Nz = p + 1

    margin_left = 50
    margin_right = 200

    char_width = 50
    char_height = 40
    """一文字の幅の目安"""

    grundy_sequence = GrundySequence.make(S={a, b, c}, len_N=len_Nz-1)
    """グランディ数列"""

    image_width = int(
        (len_Nz * char_width + margin_left + margin_right) * zoom)
    image_height = int(char_height*13*zoom)

    # 画像データは数値の配列
    monochrome_color = 240  # 0黒→255白
    canvas = np.full((image_height, image_width, 3),
                     monochrome_color, dtype=np.uint8)

    font_color = (55, 55, 55)
    color_red = (90, 90, 220)
    color_green = (90, 220, 90)
    color_blue = (220, 90, 90)
    """色"""

    line_thickness = 1
    """線の太さ"""

    if a % 2 == 0:
        eo_a = "E"
    else:
        eo_a = "o"

    if b % 2 == 0:
        eo_b = "E"
    else:
        eo_b = "o"

    if c % 2 == 0:
        eo_c = "E"
    else:
        eo_c = "o"

    eo_code = f"{eo_a}{eo_b}{eo_c}"
    """偶奇も付けたい。文字が潰れると見分けにくいので e の方を大文字にした"""

    board = [""] * len_Nz
    """盤"""

    slope_lines = []
    """坂道の線"""

    def add_slope_line(i, s, s_index):
        dst_s = i-s
        if 0 <= dst_s:
            if board[dst_s] == "":
                stone_symbol = stone_symbolds[s_index]
                board[i] += stone_symbol
                slope_lines.append((stone_symbol, i, dst_s))
        pass

    # 駒の配置 と mate線 の算出
    for i in range(0, len_Nz):
        add_slope_line(i, a, 0)
        add_slope_line(i, b, 1)
        add_slope_line(i, c, 2)

    for i in range(0, len_Nz):
        if board[i] == "":
            board[i] = "."

    def print_subtraction_set(y):
        """サブトラクションセットを表示"""
        cv2.putText(canvas,
                    f"S = {{ {a}, {b}, {c} }} {eo_code} {suffix}",
                    (int((5+margin_left)*zoom), int(y*zoom)),  # x,y
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

        #dame_color_sequence = DameColorSequence.make(grundy_sequence)

        for i in range(0, len_Nz):
            grundy_number = grundy_sequence.get_grundy_at(i)

            if grundy_number == 0:
                label = "x"  # TODO ×に色付けたい。両端の a,b,c （c優先）が同じとき、その色。それ以外は黒
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
        for mate_line in slope_lines:
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

    if suffix != "":
        suffix_text = f"_{suffix}"
    else:
        suffix_text = ""

    if is_temporary:
        tmp_text = "_tmp"
    else:
        tmp_text = ""

    # date = datetime.now().strftime("%Y%m%d_%H%M%S")
    cv2.imwrite(
        f"./output_tmp/s_{a:02}_{b:02}_{c:02}_{eo_code}{suffix_text}{tmp_text}.png", canvas)

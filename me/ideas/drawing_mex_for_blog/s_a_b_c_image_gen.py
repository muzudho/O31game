import cv2
import numpy as np
# from datetime import datetime
from kernel.math.grundy_sequence import GrundySequence


def gen_s_a_b_c_image(a, b, c, len_Nz, zoom=1.0, suffix="", is_temporary=True):
    """
    Parameters
    ----------
    zoom : float
        描画倍率
    """

    margin_left = 5
    margin_right = 5
    margin_top = 5
    margin_bottom = 5

    grid_width = 48
    grid_height = 48
    """グリッドサイズ。半角２文字入るぐらいを１セルにしたい"""

    grid_columns = 21
    grid_rows = 15
    char_base_y = int(grid_height*0.9)
    """一文字の幅の目安"""

    grundy_sequence = GrundySequence.make(S={a, b, c}, len_N=len_Nz-1)
    """グランディ数列"""

    image_width = int(
        (len_Nz * grid_width + margin_left + margin_right) * zoom)
    image_height = int(grid_height*16*zoom)

    # 画像データは数値の配列
    monochrome_color = 240  # 0黒→255白
    canvas = np.full((image_height, image_width, 3),
                     monochrome_color, dtype=np.uint8)

    font_color = (55, 55, 55)
    color_red = (90, 90, 220)
    color_green = (90, 220, 90)
    color_blue = (220, 90, 90)
    color_yellow_green = (153, 220, 192)
    color_cyan = (220, 220, 192)
    color_magenta = (220, 192, 220)
    color_yellow = (192, 220, 220)
    color_light_grey = (220, 220, 220)
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

    top_a_board = [-1] * len_Nz
    top_b_board = [-1] * len_Nz
    top_c_board = [-1] * len_Nz
    """番地の上側に置いてある数"""

    mate_lines = []
    """mate線"""

    # 駒の配置 と mate線 の算出
    for top_n in range(0, len_Nz):
        bottom_a = top_n-a
        bottom_b = top_n-b
        bottom_c = top_n-c
        if 0 <= bottom_a:
            top_a_board[top_n] = grundy_sequence.get_grundy_at(bottom_a)
            mate_lines.append(("a", top_n, bottom_a))

        if 0 <= bottom_b:
            top_b_board[top_n] = grundy_sequence.get_grundy_at(bottom_b)
            mate_lines.append(("b", top_n, bottom_b))

        if 0 <= bottom_c:
            top_c_board[top_n] = grundy_sequence.get_grundy_at(bottom_c)
            mate_lines.append(("c", top_n, bottom_c))

    def draw_grid():
        """グリッドを描画"""

        for i in range(0, grid_columns):
            """垂直線"""

            x = int((i*grid_width+margin_left)*zoom)
            top_y = int((margin_top)*zoom)
            bottom_y = int((grid_rows*grid_height+margin_top)*zoom)

            cv2.line(canvas,
                     (x, top_y),
                     (x, bottom_y),
                     color_light_grey,
                     thickness=line_thickness)

        for j in range(0, grid_rows):
            """水平線"""

            y = int((j*grid_height+margin_top)*zoom)
            left_x = int((margin_left)*zoom)
            right_x = int((grid_columns*grid_width+margin_left)*zoom)

            cv2.line(canvas,
                     (left_x, y),
                     (right_x, y),
                     color_light_grey,
                     thickness=line_thickness)

    def print_subtraction_set(y):
        """サブトラクションセットを表示"""
        cv2.putText(canvas,
                    f"S = {{ {a}, {b}, {c} }} {eo_code} {suffix}",
                    (int(5*zoom), int(y*zoom) + int(char_base_y*zoom)),  # x,y
                    None,  # font
                    1.0 * zoom,  # font_scale
                    font_color,  # color
                    0)  # line_type

    def print_grundy_color_rectangle(x, y, grundy_number):
        """グランディ数を色付きの四角で描画"""

        if grundy_number == 0:
            color_rectangle = color_yellow_green
        elif grundy_number == 1:
            color_rectangle = color_cyan
        elif grundy_number == 2:
            color_rectangle = color_magenta
        elif grundy_number == 3:
            color_rectangle = color_yellow
        else:
            raise ValueError(f"unexpected grundy number:{grundy_number}")
        """グランディ色"""

        dx = x + int(grid_width*zoom)
        dy = y + int(grid_height*zoom)
        cv2.rectangle(img=canvas,
                      pt1=(x, y),  # left, top
                      pt2=(dx, dy),  # right, bottom
                      color=color_rectangle,  # color
                      thickness=-1)  # fill: -1

    def paint_row_of_zero_number(y):
        """0 の行を描画"""

        for i in range(0, len_Nz):
            if top_a_board[i] == -1 and top_b_board[i] == -1 and top_c_board[i] == -1:
                grundy_number = 0
                sx = int((i*grid_width+margin_left)*zoom)
                sy = int(y*zoom)

                print_grundy_color_rectangle(
                    x=sx,
                    y=sy,
                    grundy_number=grundy_number)
                """グランディ数に対応づく色の四角"""

                cv2.putText(canvas,
                            f"0",
                            (sx, sy + int(char_base_y*zoom)),  # x,y
                            None,  # font
                            1.0 * zoom,  # font_scale
                            font_color,  # color
                            0)  # line_type

    def print_row_of_a_number(y):
        """駒を描画"""
        for i in range(0, len_Nz):
            grundy_number = top_a_board[i]  # -1: None
            if grundy_number != -1:
                sx = int((i*grid_width+margin_left)*zoom)
                sy = int(y*zoom)

                print_grundy_color_rectangle(
                    x=sx,
                    y=sy,
                    grundy_number=grundy_number)
                """グランディ数に対応づく色の四角"""

                cv2.putText(canvas,
                            f"{grundy_number}",
                            (sx, sy + int(char_base_y*zoom)),  # x,y
                            None,  # font
                            1.0 * zoom,  # font_scale
                            color_red,  # color
                            0)  # line_type

    def print_row_of_b_number(y):
        """駒を描画"""
        for i in range(0, len_Nz):
            grundy_number = top_b_board[i]  # -1: None
            if grundy_number != -1:
                sx = int((i*grid_width+margin_left)*zoom)
                sy = int(y*zoom)

                print_grundy_color_rectangle(
                    x=sx,
                    y=sy,
                    grundy_number=grundy_number)
                """グランディ数に対応づく色の四角"""

                cv2.putText(canvas,
                            f"{grundy_number}",
                            (sx, sy + int(char_base_y*zoom)),  # x,y
                            None,  # font
                            1.0 * zoom,  # font_scale
                            color_green,  # color
                            0)  # line_type

    def print_row_of_c_number(y):
        """駒を描画"""
        for i in range(0, len_Nz):
            grundy_number = top_c_board[i]  # -1: None
            if grundy_number != -1:
                sx = int((i*grid_width+margin_left)*zoom)
                sy = int(y*zoom)

                print_grundy_color_rectangle(
                    x=sx,
                    y=sy,
                    grundy_number=grundy_number)
                """グランディ数に対応づく色の四角"""

                cv2.putText(canvas,
                            f"{grundy_number}",
                            (sx, sy + int(char_base_y*zoom)),  # x,y
                            None,  # font
                            1.0 * zoom,  # font_scale
                            color_blue,  # color
                            0)  # line_type

    def print_x_axis(y):
        """x軸を描画"""
        for i in range(0, len_Nz):
            cv2.putText(canvas,
                        f"{i}",
                        (int((i*grid_width+margin_left)*zoom), int(y*zoom)),  # x,y
                        None,  # font
                        1.0 * zoom,  # font_scale
                        font_color,  # color
                        0)  # line_type

    def print_grundy_sequence(y):
        """グランディ数列を図形的に描画"""

        for i in range(0, len_Nz):
            sx = int((i*grid_width+margin_left)*zoom)

            grundy_number = grundy_sequence.get_grundy_at(i)

            print_grundy_color_rectangle(
                x=sx,
                y=int((y-grid_height)*zoom),
                grundy_number=grundy_number)
            """グランディ数に対応づく色の四角"""

            if grundy_number == 0:
                label = "x"  # TODO ×に色付けたい。両端の a,b,c （c優先）が同じとき、その色。それ以外は黒
                vertical_repeat = 1

            else:
                label = "."
                vertical_repeat = grundy_number

            for j in range(0, vertical_repeat):  # 文字を上にずらしながら重ねていく
                cv2.putText(canvas,
                            label,
                            (sx,
                             int((y-(grid_height/4)*j)*zoom)),  # x,y
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
            src_x = int((grid_width*src_i+margin_left)*zoom)

            dst_i = mate_line[2]
            dst_x = int((grid_width*dst_i+margin_left)*zoom)

            cv2.line(canvas, (src_x, int(src_y*zoom)),
                     (dst_x, int(dst_y*zoom)), line_color, thickness=line_thickness)

    draw_grid()
    """グリッドを描画"""

    y = 0
    print_subtraction_set(y=y)
    y += grid_height
    """サブトラクションセットを表示"""

    print_row_of_c_number(y=y)
    y += grid_height
    """駒を描画"""

    print_row_of_b_number(y=y)
    y += grid_height
    """駒を描画"""

    print_row_of_a_number(y=y)
    """駒を描画"""

    paint_row_of_zero_number(y=y)
    y += grid_height
    """重ねて 0 の行を描画"""

    y += 20  # 180, 450
    print_mate_lins(src_y=y, dst_y=y+270)
    """mate線を描画"""

    y += 310  # 470
    print_grundy_sequence(y=y)

    y += grid_height  # 530
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

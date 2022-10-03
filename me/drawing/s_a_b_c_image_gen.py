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
    image_width = int(image_width/2)  # 全体を入れるのではなく、左半分ぐらいを画像にする
    image_height = int(char_width*10*zoom)

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

    occupied_bitboard = [False] * len_Nz
    """オキュパイド ビット盤"""

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

    for i in range(0, len_Nz):
        if board[i] != "":
            occupied_bitboard[i] = True

    def print_empty_pieces(y):
        """駒を描画"""
        for i in range(0, len_Nz):
            if board[i] == ".":
                cv2.putText(canvas,
                            f".",
                            (int((i*char_width+margin_left)*zoom), y),  # x,y
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
                            (int((i*char_width+margin_left)*zoom), y),  # x,y
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
                            (int((i*char_width+margin_left)*zoom), y),  # x,y
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
                            (int((i*char_width+margin_left)*zoom), y),  # x,y
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

            cv2.line(canvas, (src_x, src_y),
                     (dst_x, dst_y), line_color, thickness=line_thickness)

    def match_partial(array1, begin1, array2, begin2, length):
        for i in range(0, length):
            if array1[begin1 + i] != array2[begin2 + i]:
                return False

        return True

    def find_period():
        """周期を調べる"""

        # 最初の２つのパターン
        begin = 0

        for step in range(2, int(len_Nz/2)):
            """周期の長さを少しずつ広げていく"""
            end = begin + step
            pattern = occupied_bitboard[begin:end]

            for phase_offset in range(0, step):
                """位相のずれを考慮"""

                match_count = 0

                for i in range(end+phase_offset, len_Nz, step):
                    if i+step < len_Nz:
                        if not match_partial(occupied_bitboard, i, pattern, 0, step):
                            break

                        match_count += 1
                    elif 0 < match_count:
                        # なるべく最後の方まで見て、周期が続いていたら
                        return step

        return "-9999"
        """見つからなかった"""

    maybe_period = find_period()

    # サブトラクションセットを表示
    cv2.putText(canvas,
                f"S = {{ {a}, {b}, {c} }} Maybe period:{maybe_period}",
                (int(5*zoom), int(30*zoom)),  # x,y
                None,  # font
                1.0 * zoom,  # font_scale
                font_color,  # color
                0)  # line_type

    print_c_pieces(y=int(90*zoom))
    """駒を描画"""

    print_b_pieces(y=int(130*zoom))
    """駒を描画"""

    print_a_pieces(y=int(170*zoom))
    print_empty_pieces(y=int(170*zoom))
    """駒を描画"""

    print_mate_lins(src_y=int(190*zoom), dst_y=int(460*zoom))
    """mate線を描画"""

    print_occupied_pieces(y=int(480*zoom))
    """駒の有無を描画"""

    print_x_axis(y=int(520*zoom))
    """x軸を描画"""

    # date = datetime.now().strftime("%Y%m%d_%H%M%S")
    cv2.imwrite(f"./output/s_{a}_{b}_{c}_tmp.png", canvas)

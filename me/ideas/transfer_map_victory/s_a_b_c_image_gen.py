"""
pip install opencv-python
pip install Pillow

cd me

python.exe -m ideas.vector_coordinate.main
"""
import cv2
import numpy as np
from kernel.math.eo_code import EoCode
from kernel.math.music_chord import MusicChord
from ideas.transfer_map_victory.grundy_graph import GrundyGraph
from ideas.transfer_map_victory.nim_constants import nim_constants


def gen_s_a_b_c_image(a, b, c, zoom=1.0, is_temporary=True):
    """
    a < b < c

    Parameters
    ----------
    zoom : float
        倍率。1倍はかなりでかい
    """

    eo_code = EoCode.stringify(a, b, c)
    music_chord = MusicChord.stringify(a, b, c)
    display_max_number = 50

    is_visibled_a_line = True
    is_visibled_b_line = True
    is_visibled_c_line = True
    """線の描画の有無"""

    d_a_b = b-a
    d_b_c = c-b
    d_c_apb = c-(a+b)
    minimum_d = min([d_a_b, d_b_c, d_c_apb])
    maximum_d = max([d_a_b, d_b_c, d_c_apb])
    """a,b,cの間隔"""

    # if d_a_b <= d_b_c or d_a_b <= d_c_apb:
    #    is_visibled_a_line = False

    # if d_b_c <= d_a_b or d_b_c <= d_c_apb:
    #    is_visibled_b_line = False

    # if d_c_apb <= d_a_b or d_c_apb <= d_b_c:
    #    is_visibled_c_line = False
    """一番間隔の狭い線を非表示"""

    hc = a+b
    hb = 0  # bは水平
    ha = a  # aはナナメ
    """width と height"""

    margin_left = 20
    margin_right = 5
    margin_top = 150
    margin_bottom = 5

    columns = 50
    rows = 50
    drawing_columns = 50
    drawing_rows = 50

    char_base_width = -10
    char_base_height = 5
    char_width = 50
    char_height = 50
    """一文字の幅の目安"""

    color_black = (55, 55, 55)  # (B,G,R)
    color_red = (90, 90, 220)
    color_green = (90, 220, 90)
    color_blue = (220, 90, 90)
    color_cyan = (220, 220, 90)
    color_magenta = (220, 90, 220)
    color_yellow = (90, 220, 220)
    """色"""

    line_thickness = 1
    """線の太さ"""

    def make_image():
        image_width = int(
            (columns * char_width + margin_left + margin_right) * zoom)
        image_height = int(
            (rows * char_height+margin_top + margin_bottom)*2/3*zoom)

        # 画像データは数値の配列
        monochrome_color = 240  # 0黒→255白
        canvas = np.full((image_height, image_width, 3),
                         monochrome_color, dtype=np.uint8)

        # モデル作成
        grundy_graph = GrundyGraph.make(
            drawing_columns=drawing_columns,
            drawing_rows=drawing_rows,
            a=a,
            b=b,
            c=c,
            ha=ha,
            hb=hb,
            hc=hc)

        draw_subtraction_set(canvas, (0, 0))
        """サブストラクションセット描画"""

        draw_x_stone(canvas, grundy_graph.root_point)
        """根の点描画"""

        for hash_key in grundy_graph.tp_table.keys():
            """三本毛の描画"""
            trident = grundy_graph.tp_table.get_trident(hash_key)
            draw_trident(canvas, trident, grundy_graph)

        if music_chord != "":
            music_chord_text = f"_{music_chord}"
        else:
            music_chord_text = ""

        if is_temporary:
            tmp_text = "_tmp"
        else:
            tmp_text = ""

        cv2.imwrite(
            f"./output_tmp/transfer_map_spin_s_{a:02}_{b:02}_{c:02}_{eo_code}{music_chord_text}{tmp_text}.png", canvas)
        """画像出力"""

    def draw_subtraction_set(canvas, point):
        """サブトラクションセットを表示"""
        x = point[0]
        y = point[1]
        location = (int((x+char_base_width+margin_left)*zoom),
                    int((y+char_base_height+margin_left)*4*zoom))
        font_scale = 4.0 * zoom

        cv2.putText(canvas,
                    f"S = {{   ,   ,    }} {eo_code} {music_chord}",
                    location,  # x,y
                    None,  # font
                    font_scale,  # font_scale
                    color_black,  # color
                    0)  # line_type

        cv2.putText(canvas,
                    f"      {a:2}",
                    location,  # x,y
                    None,  # font
                    font_scale,  # font_scale
                    color_red,  # color
                    0)  # line_type

        cv2.putText(canvas,
                    f"          {b:2}",
                    location,  # x,y
                    None,  # font
                    font_scale,  # font_scale
                    color_green,  # color
                    0)  # line_type

        cv2.putText(canvas,
                    f"              {c:2}",
                    location,  # x,y
                    None,  # font
                    font_scale,  # font_scale
                    color_blue,  # color
                    0)  # line_type

    def draw_trident(canvas, trident, grundy_graph):
        """三本毛を描く"""

        sx = trident.src_point[0]
        stonecolor_begin = grundy_graph.grundy_sequence.get_grundy_at(sx)
        ax = trident.a_point[0]
        stonecolor_end_a = grundy_graph.grundy_sequence.get_grundy_at(ax)
        bx = trident.b_point[0]
        stonecolor_end_b = grundy_graph.grundy_sequence.get_grundy_at(bx)
        cx = trident.c_point[0]
        stonecolor_end_c = grundy_graph.grundy_sequence.get_grundy_at(cx)
        """始点の石の色"""

        # 終点a
        draw_stone(canvas, trident.a_point,
                   get_color_from_stonecolor(grundy_graph.stone_sequence.get_largest_stonecolor_at(ax)))
        """a石の描画"""

        if is_visibled_a_line:
            """s-->a線の描画"""
            # 始点と終点の組み合わせによって色を変える
            draw_line(canvas, trident.src_point, trident.a_point,
                      get_color_from_2stones_color(stonecolor_begin, stonecolor_end_a))

        """a石と、s-->a線の描画"""

        # 終点b
        draw_stone(canvas, trident.b_point,
                   get_color_from_stonecolor(grundy_graph.stone_sequence.get_largest_stonecolor_at(bx)))
        """b石の描画"""

        if is_visibled_b_line:
            """s-->b線の描画"""
            draw_line(canvas, trident.src_point, trident.b_point,
                      get_color_from_2stones_color(stonecolor_begin, stonecolor_end_b))

        """b石と、s-->b線の描画"""

        # 終点c
        draw_stone(canvas, trident.c_point,
                   get_color_from_stonecolor(grundy_graph.stone_sequence.get_largest_stonecolor_at(cx)))
        """c石の描画"""

        if is_visibled_c_line:
            """s-->c線の描画"""
            draw_line(canvas, trident.src_point, trident.c_point,
                      get_color_from_2stones_color(stonecolor_begin, stonecolor_end_c))

        """c石と、s-->c線の描画"""

    def get_color_from_stonecolor(stonecolor):
        if stonecolor == nim_constants.stonecolor_x:
            return color_black

        if stonecolor == nim_constants.stonecolor_a:
            return color_red

        if stonecolor == nim_constants.stonecolor_b:
            return color_green

        if stonecolor == nim_constants.stonecolor_c:
            return color_blue

        raise ValueError(f"unexpected stonecolor:{stonecolor}")

    def get_color_from_2stones_color(smaller_stonecolor, larger_stonecolor):
        """始点の色と、終点の色の組み合わせによって色を変えます"""
        if smaller_stonecolor == larger_stonecolor:
            return get_color_from_stonecolor(smaller_stonecolor)

        if smaller_stonecolor == nim_constants.stonecolor_x:
            """小さい方の石が グランディ数 0 なら、線は大きい方の数に従う"""
            return get_color_from_stonecolor(larger_stonecolor)

        if larger_stonecolor == nim_constants.stonecolor_x:
            """大きい方の石が グランディ数 0 なら、線はグランディ数 0 の方に従う"""
            return get_color_from_stonecolor(nim_constants.stonecolor_x)

        if (smaller_stonecolor == nim_constants.stonecolor_a and larger_stonecolor == nim_constants.stonecolor_b) or (smaller_stonecolor == nim_constants.stonecolor_b and larger_stonecolor == nim_constants.stonecolor_a):
            return color_yellow

        if (smaller_stonecolor == nim_constants.stonecolor_b and larger_stonecolor == nim_constants.stonecolor_c) or (smaller_stonecolor == nim_constants.stonecolor_c and larger_stonecolor == nim_constants.stonecolor_b):
            return color_cyan

        if (smaller_stonecolor == nim_constants.stonecolor_c and larger_stonecolor == nim_constants.stonecolor_a) or (smaller_stonecolor == nim_constants.stonecolor_a and larger_stonecolor == nim_constants.stonecolor_c):
            return color_magenta

        return get_color_from_stonecolor(nim_constants.stonecolor_x)

    def draw_x_stone(canvas, point):
        """x石を描く"""
        x = point[0]
        y = point[1]
        cv2.putText(canvas,
                    "x",
                    (int((x*char_width+char_base_width+margin_left)*zoom),
                     int((y*char_height+char_base_height+margin_top)*zoom)),  # x,y
                    None,  # font
                    zoom,  # font_scale
                    color_black,  # color
                    0)  # line_type

    def draw_stone(canvas, point, color_stone):
        """石を描く"""
        x = point[0]
        y = point[1]

        if x <= display_max_number:
            label = f"{x}"
        else:
            label = ""

        cv2.putText(canvas,
                    label,
                    (int((x*char_width+char_base_width+margin_left)*zoom),
                     int((y*char_height+char_base_height+margin_top)*zoom)),  # x,y
                    None,  # font
                    zoom,  # font_scale
                    color_stone,  # color
                    0)  # line_type

    def draw_line(canvas, src_point, dst_point, color_line):
        """線の描画"""
        sx = src_point[0]
        sy = src_point[1]
        dx = dst_point[0]
        dy = dst_point[1]
        cv2.line(canvas, (int((sx*char_width+margin_left)*zoom), int((sy*char_height+margin_top)*zoom)),
                 (int((dx*char_width+margin_left)*zoom), int((dy*char_height+margin_top)*zoom)), color_line, thickness=line_thickness)

    make_image()

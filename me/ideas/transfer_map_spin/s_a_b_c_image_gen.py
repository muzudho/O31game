"""
pip install opencv-python
pip install Pillow

cd me

python.exe -m ideas.vector_coordinate.main
"""
from multiprocessing.sharedctypes import Value
import cv2
import numpy as np
from kernel.math.eo_code import EoCode
from kernel.math.music_chord import MusicChord
from ideas.transfer_map_spin.trident_hair import TridentHair
from ideas.transfer_map_spin.grundy_graph import GrundyGraph

stonecolor_x = 0
stonecolor_a = 1
stonecolor_b = 2
stonecolor_c = 3
"""石の色"""


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
    drawing_columns = 10
    drawing_rows = 10

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
    color_line_x = color_black
    color_line_a = color_red
    color_line_b = color_green
    color_line_c = color_blue
    color_line_a_b = color_yellow  # color of light
    color_line_b_c = color_cyan
    color_line_c_a = color_magenta
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
        grundy_graph = GrundyGraph()

        make_each_tridents_from(
            grundy_graph.root_point, grundy_graph.tp_table, stonecolor_x, grundy_graph.src_color_table)

        draw_subtraction_set(canvas, (0, 0))
        """サブストラクションセット描画"""

        draw_x_stone(canvas, grundy_graph.root_point)
        """根の点描画"""

        for hash_key in grundy_graph.tp_table.keys():
            """三本毛の描画"""
            trident = grundy_graph.tp_table.get_trident(hash_key)
            draw_trident(canvas, trident, grundy_graph.src_color_table)

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

    def make_each_tridents_from(src_point, tp_table, src_stonecolor, src_color_table):
        trident = TridentHair.make(
            src_point,
            columns=drawing_columns,
            rows=drawing_rows,
            a=a,
            b=b,
            c=c,
            ha=ha,
            hb=hb,
            hc=hc)

        if trident is not None:
            """指定の範囲内のみ描画"""

            hash_key = trident.create_hash()
            print(f"src({trident.src_point}) hash_key:{hash_key}")

            if not tp_table.contains_key(hash_key):
                """存在しない三本毛なら登録"""
                tp_table.add_trident(hash_key, trident)
                src_color_table.add_stonecolor(
                    trident.src_point, src_stonecolor)
                print(
                    f"新規　 src({trident.src_point}) src_stonecolor:{src_stonecolor}")

                make_each_tridents_from(
                    trident.a_point, tp_table, stonecolor_a, src_color_table)
                """a点から生えている三本毛"""

                make_each_tridents_from(
                    trident.b_point, tp_table, stonecolor_b, src_color_table)
                """b点から生えている三本毛"""

                make_each_tridents_from(
                    trident.c_point, tp_table, stonecolor_c, src_color_table)
                """c点から生えている三本毛"""
            else:
                """存在する三本毛なら"""
                exist_src_stonecolor = src_color_table.get_stonecolor(
                    trident.src_point)
                if exist_src_stonecolor < src_stonecolor:
                    """上書きできる石の色なら"""
                    src_color_table.add_stonecolor(
                        trident.src_point, src_stonecolor)  # Update
                    print(
                        f"上書き src({trident.src_point}) exist_src_stonecolor:{exist_src_stonecolor} src_stonecolor:{src_stonecolor}")
                else:
                    print(
                        f"無視　 src({trident.src_point}) exist_src_stonecolor:{exist_src_stonecolor} src_stonecolor:{src_stonecolor}")

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

    def draw_trident(canvas, trident, src_color_table):
        """三本毛を描く"""
        global stonecolor_x, stonecolor_a, stonecolor_b, stonecolor_c

        if src_color_table.contains_key(trident.src_point):
            stonecolor_begin = src_color_table.get_stonecolor(
                trident.src_point)
        else:
            stonecolor_begin = stonecolor_x

        # 始点と終点の組み合わせによって色を変える

        # 終点a
        draw_stone(canvas, trident.a_point, color_red)
        """a石の描画"""

        if stonecolor_begin == stonecolor_x:
            color_line = color_line_x
        elif stonecolor_begin == stonecolor_a:
            color_line = color_line_a
        elif stonecolor_begin == stonecolor_b:
            color_line = color_line_a_b
        elif stonecolor_begin == stonecolor_c:
            color_line = color_line_c_a
        else:
            raise ValueError(f"unexpected stonecolor_begin:{stonecolor_begin}")
        print(
            f"s-->a線描画 stonecolor_begin:{stonecolor_begin} color_line:{color_line}")

        if is_visibled_a_line:
            """s-->a線の描画"""
            draw_line(canvas, trident.src_point, trident.a_point, color_line)

        """a石と、s-->a線の描画"""

        # 終点b
        draw_stone(canvas, trident.b_point, color_green)
        """b石の描画"""

        if stonecolor_begin == stonecolor_x:
            color_line = color_line_x
        elif stonecolor_begin == stonecolor_a:
            color_line = color_line_a_b
        elif stonecolor_begin == stonecolor_b:
            color_line = color_line_b
        elif stonecolor_begin == stonecolor_c:
            color_line = color_line_c_a
        else:
            raise ValueError(f"unexpected stonecolor_begin:{stonecolor_begin}")

        # if is_visibled_b_line:
            """s-->b線の描画"""
            #draw_line(canvas, trident.src_point, trident.b_point, color_line)

        """b石と、s-->b線の描画"""

        # 終点c
        draw_stone(canvas, trident.c_point, color_blue)
        """c石の描画"""

        if stonecolor_begin == stonecolor_x:
            color_line = color_line_x
        elif stonecolor_begin == stonecolor_a:
            color_line = color_line_a_b
        elif stonecolor_begin == stonecolor_b:
            color_line = color_line_b_c
        elif stonecolor_begin == stonecolor_c:
            color_line = color_line_c
        else:
            raise ValueError(f"unexpected stonecolor_begin:{stonecolor_begin}")

        # if is_visibled_c_line:
            """s-->c線の描画"""
            #draw_line(canvas, trident.src_point, trident.c_point, color_line)

        """c石と、s-->c線の描画"""

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

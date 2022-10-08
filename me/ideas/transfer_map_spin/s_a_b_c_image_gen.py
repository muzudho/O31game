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
from ideas.transfer_map_spin.trident_hair import TridentHair
from ideas.transfer_map_spin.transposition_table import TranspositionTable


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
    """a,b,cの間隔"""

    if d_a_b <= d_b_c or d_a_b <= d_c_apb:
        is_visibled_a_line = False

    if d_b_c <= d_a_b or d_b_c <= d_c_apb:
        is_visibled_b_line = False

    if d_c_apb <= d_a_b or d_c_apb <= d_b_c:
        is_visibled_c_line = False
    """一番間隔の狭い線を非表示"""

    wa = 2*a  # weight a
    wb = 2*b
    wc = 2*c

    hc = a+b
    hb = 0  # bは水平
    ha = a  # aはナナメ
    """width と height"""

    margin_left = 20
    margin_right = 5
    margin_top = 100
    margin_bottom = 5

    columns = 100
    rows = 100

    char_base_width = -10
    char_base_height = 5
    char_width = 50
    char_height = 50
    """一文字の幅の目安"""

    color_black = (55, 55, 55)
    color_red = (90, 90, 220)
    color_green = (90, 220, 90)
    color_blue = (220, 90, 90)
    color_cyan = (90, 220, 220)
    color_magenta = (220, 90, 220)
    color_yellow = (220, 220, 90)
    color_line_a = color_cyan
    color_line_b = color_magenta
    color_line_c = color_yellow
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
        tp_table = TranspositionTable()
        """三本毛のテーブル"""
        src_stone_table = dict()
        """重なる始点の優先色テーブル"""

        root_point = {"x": 0, "y": 1}
        """根の点"""

        make_some_next_nodes_from(root_point, tp_table)

        paint_subtraction_set(canvas, 0, 0)
        """サブストラクションセット描画"""

        paint_x_stone(canvas, root_point)
        """根の点描画"""

        for hash_key in tp_table.table.keys():
            """a毛の描画"""
            paint_a_hair(canvas, tp_table.table[hash_key])

        for hash_key in tp_table.table.keys():
            """b毛の描画"""
            paint_b_hair(canvas, tp_table.table[hash_key])

        for hash_key in tp_table.table.keys():
            """c毛の描画"""
            paint_c_hair(canvas, tp_table.table[hash_key])

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

    def make_some_next_nodes_from(src_point, tp_table):
        trident = TridentHair.make(
            src_point,
            columns=columns,
            rows=rows,
            wa=wa,
            wb=wb,
            wc=wc,
            ha=ha,
            hb=hb,
            hc=hc)

        if trident is not None:
            hash_key = trident.create_hash()
            if not (hash_key in tp_table.table):
                tp_table.add_trident(hash_key, trident)

                make_some_next_nodes_from(trident.a_point, tp_table)
                """a点から生えている三本毛"""

                make_some_next_nodes_from(trident.b_point, tp_table)
                """b点から生えている三本毛"""

                make_some_next_nodes_from(trident.c_point, tp_table)
                """c点から生えている三本毛"""

    def paint_subtraction_set(canvas, x, y):
        """サブトラクションセットを表示"""
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

    def paint_3_hairs(canvas, trident):
        """三本毛を描く"""

        paint_a_hair(canvas, trident)
        """a石と、x-->a線の描画"""

        paint_a_hair(canvas, trident)
        """b石と、x-->b線の描画"""

        paint_a_hair(canvas, trident)
        """c石と、x-->c線の描画"""

    def paint_a_hair(canvas, trident):
        """a毛を描く"""

        paint_a_stone(canvas, trident.a_point)
        """a石の描画"""

        if is_visibled_a_line:
            """x-->a線の描画"""
            draw_line(canvas, trident.src_point, trident.a_point, color_line_a)

    def paint_b_hair(canvas, trident):
        """b毛を描く"""

        paint_b_stone(canvas, trident.b_point)
        """b石の描画"""

        if is_visibled_b_line:
            """x-->b線の描画"""
            draw_line(canvas, trident.src_point, trident.b_point, color_line_b)

    def paint_c_hair(canvas, trident):
        """c毛を描く"""

        paint_c_stone(canvas, trident.c_point)
        """c石の描画"""

        if is_visibled_c_line:
            """x-->c線の描画"""
            draw_line(canvas, trident.src_point, trident.c_point, color_line_c)

    def paint_x_stone(canvas, point):
        """x石を描く"""
        x = point["x"]
        y = point["y"]
        cv2.putText(canvas,
                    "x",
                    (int((x*char_width+char_base_width+margin_left)*zoom),
                     int((y*char_height+char_base_height+margin_top)*zoom)),  # x,y
                    None,  # font
                    zoom,  # font_scale
                    color_black,  # color
                    0)  # line_type

    def paint_a_stone(canvas, point):
        """a石を描く"""
        x = point["x"]
        y = point["y"]

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
                    color_red,  # color
                    0)  # line_type

    def paint_b_stone(canvas, point):
        """b石を描く"""
        x = point["x"]
        y = point["y"]

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
                    color_green,  # color
                    0)  # line_type

    def paint_c_stone(canvas, point):
        """c石を描く"""
        x = point["x"]
        y = point["y"]

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
                    color_blue,  # color
                    0)  # line_type

    def draw_line(canvas, src_point, dst_point, color_line):
        """線の描画"""
        sx = src_point["x"]
        sy = src_point["y"]
        dx = dst_point["x"]
        dy = dst_point["y"]
        cv2.line(canvas, (int((sx*char_width+margin_left)*zoom), int((sy*char_height+margin_top)*zoom)),
                 (int((dx*char_width+margin_left)*zoom), int((dy*char_height+margin_top)*zoom)), color_line, thickness=line_thickness)

    make_image()

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

    if d_a_b <= d_c_apb and d_b_c <= d_c_apb:
        is_visibled_a_line = False
        is_visibled_b_line = False
        pass
    elif d_a_b <= d_b_c and d_c_apb <= d_b_c:
        is_visibled_a_line = False
        is_visibled_c_line = False
    elif d_b_c <= d_a_b and d_c_apb <= d_a_b:
        is_visibled_b_line = False
        is_visibled_c_line = False
    """一番間隔の広い線だけ描画"""

    wa = 2*a  # weight a
    wb = 2*b
    wc = 2*c

    hc = a+b
    hb = 0  # bは水平
    ha = a  # aはナナメ
    """width と height"""

    margin_left = 20
    margin_right = 5
    margin_top = 20
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
        transposition_table = dict()

        root_point = {"x": 0, "y": 1}
        """根の点"""

        make_some_next_nodes_from(root_point, transposition_table)

        paint_subtraction_set(canvas, 0, 0)
        """サブストラクションセット描画"""

        paint_x_stone(canvas, root_point)
        """根の点描画"""

        for hash_key in transposition_table.keys():
            """a毛の描画"""
            paint_a_hair(canvas, transposition_table[hash_key])

        for hash_key in transposition_table.keys():
            """b毛の描画"""
            paint_b_hair(canvas, transposition_table[hash_key])

        for hash_key in transposition_table.keys():
            """c毛の描画"""
            paint_c_hair(canvas, transposition_table[hash_key])

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

    def make_some_next_nodes_from(src_point, transposition_table):
        three_hairs = make_next_nodes_from(src_point)

        if three_hairs is not None:
            hash_key = (three_hairs[0]["x"], three_hairs[0]["y"],
                        three_hairs[1]["x"], three_hairs[1]["y"],
                        three_hairs[2]["x"], three_hairs[2]["y"],
                        three_hairs[3]["x"], three_hairs[3]["y"])
            if not (hash_key in transposition_table):
                transposition_table[hash_key] = three_hairs

                a_point = three_hairs[1]
                make_some_next_nodes_from(a_point, transposition_table)
                """a点から生えている三本毛"""

                b_point = three_hairs[2]
                make_some_next_nodes_from(b_point, transposition_table)
                """b点から生えている三本毛"""

                c_point = three_hairs[3]
                make_some_next_nodes_from(c_point, transposition_table)
                """c点から生えている三本毛"""

    def make_next_nodes_from(src_point):
        sx = src_point["x"]
        sy = src_point["y"]
        if sx < columns and sy < rows:
            a_point = {"x": sx+wa, "y": sy+ha}
            """次のa点"""

            b_point = {"x": sx+wb, "y": sy+hb}
            """次のb点"""

            c_point = {"x": sx+wc, "y": sy+hc}
            """次のc点"""

            return (src_point, a_point, b_point, c_point)

        return None

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

    def paint_3_hairs(canvas, three_hairs):
        """三本毛を描く"""

        paint_a_hair(canvas, three_hairs)
        """a石と、x-->a線の描画"""

        paint_a_hair(canvas, three_hairs)
        """b石と、x-->b線の描画"""

        paint_a_hair(canvas, three_hairs)
        """c石と、x-->c線の描画"""

    def paint_a_hair(canvas, three_hairs):
        """a毛を描く"""

        src_point = three_hairs[0]
        """始点の石"""

        a_point = three_hairs[1]

        paint_a_stone(canvas, a_point)
        """a石の描画"""

        if is_visibled_a_line:
            """x-->a線の描画"""
            paint_a_line(canvas, src_point, a_point)

    def paint_b_hair(canvas, three_hairs):
        """b毛を描く"""

        src_point = three_hairs[0]
        """始点の石"""

        b_point = three_hairs[2]

        paint_b_stone(canvas, b_point)
        """b石の描画"""

        if is_visibled_b_line:
            """x-->b線の描画"""
            paint_b_line(canvas, src_point, b_point)

    def paint_c_hair(canvas, three_hairs):
        """c毛を描く"""

        src_point = three_hairs[0]
        """始点の石"""

        c_point = three_hairs[3]

        paint_c_stone(canvas, c_point)
        """c石の描画"""

        if is_visibled_c_line:
            """x-->c線の描画"""
            paint_c_line(canvas, src_point, c_point)

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

    def paint_a_line(canvas, src_point, dst_point):
        """-->a線の描画"""
        cv2.line(canvas, (int((src_point["x"]*char_width+margin_left)*zoom), int((src_point["y"]*char_height+margin_top)*zoom)),
                 (int((dst_point["x"]*char_width+margin_left)*zoom), int((dst_point["y"]*char_height+margin_top)*zoom)), color_red, thickness=line_thickness)

    def paint_b_line(canvas, src_point, dst_point):
        """-->b線の描画"""
        cv2.line(canvas, (int((src_point["x"]*char_width+margin_left)*zoom), int((src_point["y"]*char_height+margin_top)*zoom)),
                 (int((dst_point["x"]*char_width+margin_left)*zoom), int((dst_point["y"]*char_height+margin_top)*zoom)), color_green, thickness=line_thickness)

    def paint_c_line(canvas, src_point, dst_point):
        """-->c線の描画"""
        cv2.line(canvas, (int((src_point["x"]*char_width+margin_left)*zoom), int((src_point["y"]*char_height+margin_top)*zoom)),
                 (int((dst_point["x"]*char_width+margin_left)*zoom), int((dst_point["y"]*char_height+margin_top)*zoom)), color_blue, thickness=line_thickness)

    make_image()

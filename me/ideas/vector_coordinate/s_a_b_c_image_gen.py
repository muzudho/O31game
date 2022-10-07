"""
pip install opencv-python
pip install Pillow

cd me

python.exe -m ideas.vector_coordinate.main
"""
import cv2
import numpy as np


def gen_s_a_b_c_image(a, b, c, zoom=1.0):
    """
    Parameters
    ----------
    zoom : float
        倍率。1倍はかなりでかい
    """

    ha = 2*3  # height a
    hb = 2*2
    hc = 2*1

    margin_left = 20
    margin_right = 5
    margin_top = 20
    margin_bottom = 5

    columns = 60
    rows = 60

    char_base_width = -10
    char_base_height = 5
    char_width = 50
    char_height = 40
    """一文字の幅の目安"""

    color_black = (55, 55, 55)
    color_red = (90, 90, 220)
    color_green = (90, 220, 90)
    color_blue = (220, 90, 90)
    """色"""

    line_thickness = 1
    """線の太さ"""

    rest_next_point = []
    """残りの点"""

    def make_image():
        image_width = int(
            (columns * char_width + margin_left + margin_right) * zoom)
        image_height = int(
            (rows * char_height+margin_top + margin_bottom)*zoom)

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
            """三本毛の描画"""
            paint_3_hairs(canvas, transposition_table[hash_key])

        cv2.imwrite(
            f"./output/vec_field_s_{a:02}_{b:02}_{c:02}_tmp.png", canvas)
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
            a_point = {"x": sx+a, "y": sy+ha}
            """次のa点"""

            b_point = {"x": sx+b, "y": sy+hb}
            """次のb点"""

            c_point = {"x": sx+c, "y": sy+hc}
            """次のc点"""

            return (src_point, a_point, b_point, c_point)

        return None

    def paint_subtraction_set(canvas, x, y):
        """サブトラクションセットを表示"""
        cv2.putText(canvas,
                    f"S = {{ {a}, {b}, {c} }}",
                    (int((x+char_base_width+margin_left)*zoom),
                     int((y+char_base_height+margin_left)*zoom)),  # x,y
                    None,  # font
                    1.0 * zoom,  # font_scale
                    color_black,  # color
                    0)  # line_type

    def paint_3_hairs(canvas, three_hairs):
        """三本毛を描く"""

        src_point = three_hairs[0]
        """始点の石"""

        a_point = three_hairs[1]
        b_point = three_hairs[2]
        c_point = three_hairs[3]

        paint_a_stone(canvas, a_point)
        """a石の描画"""

        paint_a_line(canvas, src_point, a_point)
        """x-->a線の描画"""

        paint_b_stone(canvas, b_point)
        """b石の描画"""

        paint_b_line(canvas, src_point, b_point)
        """x-->b線の描画"""

        paint_c_stone(canvas, c_point)
        """c石の描画"""

        paint_c_line(canvas, src_point, c_point)
        """x-->c線の描画"""

    def paint_x_stone(canvas, point):
        """x石を描く"""
        cv2.putText(canvas,
                    "x",
                    (int((point["x"]*char_width+char_base_width+margin_left)*zoom),
                     int((point["y"]*char_height+char_base_height+margin_top)*zoom)),  # x,y
                    None,  # font
                    zoom,  # font_scale
                    color_black,  # color
                    0)  # line_type

    def paint_a_stone(canvas, point):
        """a石を描く"""
        x = point["x"]
        y = point["y"]
        cv2.putText(canvas,
                    f"{x}",
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
        cv2.putText(canvas,
                    f"{x}",
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
        cv2.putText(canvas,
                    f"{x}",
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

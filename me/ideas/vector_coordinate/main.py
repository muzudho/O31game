"""
pip install opencv-python
pip install Pillow

cd me

python.exe -m ideas.vector_coordinate.main
"""
import cv2
import numpy as np


def main():
    zoom = 0.4
    """倍率。1倍はかなりでかい"""

    a = 1
    b = 3
    c = 5
    ha = 3  # height a
    hb = 2
    hc = 1

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

        # x石の描画
        x = 0
        y = 0
        paint_x_stone(canvas, x, y)
        paint_3_hairs(canvas, x, y)
        make_next_point_from(x, y)

        # while 0 < len(rest_next_point):
        for _ in range(0, 100000):
            if len(rest_next_point) < 1:
                break

            next_point = rest_next_point.pop(-1)
            paint_3_hairs(canvas, next_point["x"], next_point["y"])
            make_next_point_from(next_point["x"], next_point["y"])

        cv2.imwrite(
            f"./output/vector_coordinate_tmp.png", canvas)
        """画像出力"""

    def make_next_point_from(x, y):
        if x < 10 and y < 10:
            point = {"x": x+a, "y": y+ha}
            rest_next_point.append(point)
            """次のa点"""

            point = {"x": x+b, "y": y+hb}
            rest_next_point.append(point)
            """次のb点"""

            point = {"x": x+c, "y": y+hc}
            rest_next_point.append(point)
            """次のc点"""

    def paint_3_hairs(canvas, x, y):
        """三本毛を描く"""

        x2 = x+a
        y2 = y+ha
        paint_a_stone(canvas, x2, y2)
        """a石の描画"""

        paint_a_line(canvas, x, y, x2, y2)
        """x-->a線の描画"""

        x2 = x+b
        y2 = y+hb
        paint_b_stone(canvas, x2, y2)
        """b石の描画"""

        paint_b_line(canvas, x, y, x2, y2)
        """x-->b線の描画"""

        x2 = x+c
        y2 = y+hc
        paint_c_stone(canvas, x2, y2)
        """c石の描画"""

        paint_c_line(canvas, x, y, x2, y2)
        """x-->c線の描画"""

    def paint_x_stone(canvas, x, y):
        """x石を描く"""
        cv2.putText(canvas,
                    "x",
                    (int((x*char_width+char_base_width+margin_left)*zoom),
                     int((y*char_height+char_base_height+margin_top)*zoom)),  # x,y
                    None,  # font
                    zoom,  # font_scale
                    color_black,  # color
                    0)  # line_type

    def paint_a_stone(canvas, x, y):
        """a石を描く"""
        cv2.putText(canvas,
                    "a",
                    (int((x*char_width+char_base_width+margin_left)*zoom),
                     int((y*char_height+char_base_height+margin_top)*zoom)),  # x,y
                    None,  # font
                    zoom,  # font_scale
                    color_red,  # color
                    0)  # line_type

    def paint_b_stone(canvas, x, y):
        """b石を描く"""
        cv2.putText(canvas,
                    "b",
                    (int((x*char_width+char_base_width+margin_left)*zoom),
                     int((y*char_height+char_base_height+margin_top)*zoom)),  # x,y
                    None,  # font
                    zoom,  # font_scale
                    color_green,  # color
                    0)  # line_type

    def paint_c_stone(canvas, x, y):
        """c石を描く"""
        cv2.putText(canvas,
                    "b",
                    (int((x*char_width+char_base_width+margin_left)*zoom),
                     int((y*char_height+char_base_height+margin_top)*zoom)),  # x,y
                    None,  # font
                    zoom,  # font_scale
                    color_blue,  # color
                    0)  # line_type

    def paint_a_line(canvas, x, y, x2, y2):
        """-->a線の描画"""
        cv2.line(canvas, (int((x*char_width+margin_left)*zoom), int((y*char_height+margin_top)*zoom)),
                 (int((x2*char_width+margin_left)*zoom), int((y2*char_height+margin_top)*zoom)), color_red, thickness=line_thickness)

    def paint_b_line(canvas, x, y, x2, y2):
        """-->b線の描画"""
        cv2.line(canvas, (int((x*char_width+margin_left)*zoom), int((y*char_height+margin_top)*zoom)),
                 (int((x2*char_width+margin_left)*zoom), int((y2*char_height+margin_top)*zoom)), color_green, thickness=line_thickness)

    def paint_c_line(canvas, x, y, x2, y2):
        """-->c線の描画"""
        cv2.line(canvas, (int((x*char_width+margin_left)*zoom), int((y*char_height+margin_top)*zoom)),
                 (int((x2*char_width+margin_left)*zoom), int((y2*char_height+margin_top)*zoom)), color_blue, thickness=line_thickness)

    make_image()


if __name__ == "__main__":
    main()

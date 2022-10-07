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
        print_x_stone(canvas, x, y)

        # a石の描画
        x2 = a
        y2 = ha
        print_a_stone(canvas, x2, y2)

        # x-a線の描画
        cv2.line(canvas, (int((x*char_width+margin_left)*zoom), int((y*char_height+margin_top)*zoom)),
                 (int((x2*char_width+margin_left)*zoom), int((y2*char_height+margin_top)*zoom)), color_red, thickness=line_thickness)

        cv2.imwrite(
            f"./output/vector_coordinate_tmp.png", canvas)
        """画像出力"""

    def print_x_stone(canvas, x, y):
        cv2.putText(canvas,
                    "x",
                    (int((x*char_width+char_base_width+margin_left)*zoom),
                     int((y*char_height+char_base_height+margin_top)*zoom)),  # x,y
                    None,  # font
                    zoom,  # font_scale
                    color_black,  # color
                    0)  # line_type

    def print_a_stone(canvas, x, y):
        cv2.putText(canvas,
                    "a",
                    (int((x*char_width+char_base_width+margin_left)*zoom),
                     int((y*char_height+char_base_height+margin_top)*zoom)),  # x,y
                    None,  # font
                    zoom,  # font_scale
                    color_red,  # color
                    0)  # line_type

    make_image()


if __name__ == "__main__":
    main()

"""
pip install opencv-python
pip install Pillow

cd me

python.exe -m ideas.vector_coordinate.main
"""
import cv2
import numpy as np


def main():
    zoom = 0.25
    """倍率。1倍はかなりでかい"""

    margin_left = 5
    margin_right = 5
    margin_top = 5
    margin_bottom = 5

    columns = 50
    rows = 50

    char_width = 100
    char_height = 100
    """一文字の幅の目安"""

    image_width = int(
        (columns * char_width + margin_left + margin_right) * zoom)
    image_height = int((rows * char_height+margin_top + margin_bottom)*zoom)

    # 画像データは数値の配列
    monochrome_color = 240  # 0黒→255白
    canvas = np.full((image_height, image_width, 3),
                     monochrome_color, dtype=np.uint8)

    cv2.imwrite(
        f"./output/vector_coordinate_tmp.png", canvas)
    """画像出力"""


if __name__ == "__main__":
    main()

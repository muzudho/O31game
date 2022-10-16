"""
pip install opencv-python
pip install Pillow

cd me

python.exe -m ideas.drawing_mex.main
"""
from ideas.drawing_mex.s_a_b_c_image_gen import gen_s_a_b_c_image

zoom = 0.25
"""倍率。1倍はかなりでかい"""

len_Nz = 200
"""とりあえず c の２倍はある要素数。画像の横幅にも使われるので大きすぎないように
画像ファイルは、この半分ぐらいの部分で作ります"""


def main():
    gen_s_a_b_c_image(a=3, b=4, c=7, len_Nz=len_Nz,
                      zoom=zoom, is_temporary=False)


if __name__ == "__main__":
    main()

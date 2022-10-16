"""
pip install opencv-python
pip install Pillow

cd me

python.exe -m ideas.drawing_mex_for_blog.main
"""
from ideas.drawing_mex_for_blog.s_a_b_c_image_gen import gen_s_a_b_c_image

zoom = 0.25
"""倍率。1倍はかなりでかい"""

len_Nz = 20
"""ブログ向けなので、大きな画像は作れない"""


def main():
    gen_s_a_b_c_image(a=3, b=4, c=7, len_Nz=len_Nz,
                      zoom=zoom, is_temporary=False)


if __name__ == "__main__":
    main()

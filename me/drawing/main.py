"""
pip install opencv-python
pip install Pillow

cd me

python.exe -m drawing.main
"""
import random
from drawing.s_a_b_c_image_gen import gen_s_a_b_c_image

zoom = 0.25
"""倍率。1倍はかなりでかい"""

len_Nz = 200
"""とりあえず c の２倍はある要素数。画像の横幅にも使われるので大きすぎないように
画像ファイルは、この半分ぐらいの部分で作ります"""


def main():
    gen_s_a_b_c_image(a=3, b=8, c=10, len_Nz=len_Nz, zoom=zoom)
    # gen_odds()


def gen_odds():
    """奇数シリーズ"""
    gen_s_a_b_c_image(a=1, b=3, c=5, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=3, b=7, c=9, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=3, b=13, c=15, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=5, b=7, c=13, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=7, b=43, c=45, len_Nz=len_Nz, zoom=zoom)


def gen_3chord():
    """3和音シリーズ"""
    for ms in range(0, 12):
        """Music scale
        1: C
        2: C#
        3: D
        4: D#
        5: E
        6: F
        7: F#
        8: G
        9: G#
        10: A
        11: A#
        12: B
        """
        gen_s_a_b_c_image(a=1+ms, b=5+ms, c=8+ms, len_Nz=len_Nz, zoom=zoom)
        """メジャーコード"""

        gen_s_a_b_c_image(a=1+ms, b=4+ms, c=8+ms, len_Nz=len_Nz, zoom=zoom)
        """m マイナーコード"""

        gen_s_a_b_c_image(a=1+ms, b=6+ms, c=8+ms, len_Nz=len_Nz, zoom=zoom)
        """sus4 サスフォー"""

        gen_s_a_b_c_image(a=1+ms, b=5+ms, c=7+ms, len_Nz=len_Nz, zoom=zoom)
        """-5 フラットファイブ"""

        gen_s_a_b_c_image(a=1+ms, b=5+ms, c=9+ms, len_Nz=len_Nz, zoom=zoom)
        """aug オーギュメント"""

        gen_s_a_b_c_image(a=1+ms, b=4+ms, c=7+ms, len_Nz=len_Nz, zoom=zoom)
        """dim ディミニッシュ"""


def gen_test():
    gen_s_a_b_c_image(a=1, b=2, c=3, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=1, b=3, c=5, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=1, b=4, c=20, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=1, b=6, c=30, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=1, b=2, c=4, len_Nz=len_Nz, zoom=zoom)

    gen_s_a_b_c_image(a=1, b=3, c=7, len_Nz=len_Nz, zoom=zoom)
    """S={a,b,c} として、 S={1, 2a+1, 2b+1}"""

    gen_s_a_b_c_image(a=1, b=3, c=4, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=1, b=4, c=7, len_Nz=len_Nz, zoom=zoom)

    gen_s_a_b_c_image(a=4, b=9, c=19, len_Nz=len_Nz, zoom=zoom)


def gen_random():
    for i in range(0, 100):
        a = random.randint(1, 10)
        if 97 < a:
            a = 97
        b = a + random.randint(1, 10)
        if 98 < b:
            b = 98
        c = b + random.randint(1, 10)
        if 99 < c:
            c = 99

        gen_s_a_b_c_image(a=a, b=b, c=c, len_Nz=len_Nz, zoom=zoom)


if __name__ == "__main__":
    main()

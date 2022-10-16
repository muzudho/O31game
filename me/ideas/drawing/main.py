"""
pip install opencv-python
pip install Pillow

cd me

python.exe -m ideas.drawing.main
"""
import random
from ideas.drawing.s_a_b_c_image_gen import gen_s_a_b_c_image

zoom = 0.25
"""倍率。1倍はかなりでかい"""

len_Nz = 200
"""とりあえず c の２倍はある要素数。画像の横幅にも使われるので大きすぎないように
画像ファイルは、この半分ぐらいの部分で作ります"""


def main():
    gen_s_a_b_c_image(a=3, b=4, c=10, len_Nz=len_Nz,
                      zoom=zoom, is_temporary=False)

    # Clouds passer
    # gen_s_a_b_c_image(a=5, b=6, c=30, len_Nz=len_Nz,
    #                  zoom=zoom, is_temporary=False)
    # 5 と 6 で [5:15]

    # gen_a3_b5_c11to13()
    # gen_a_plus_b()

    # 雲の動き
    # for b in range(3, 100):
    #    gen_s_a_b_c_image(a=2, b=b, c=100, len_Nz=len_Nz,
    #                      zoom=zoom, is_temporary=False)

    # for b in range(5, 100):
    #    gen_s_a_b_c_image(a=4, b=b, c=100, len_Nz=len_Nz,
    #                      zoom=zoom, is_temporary=False)

    # 雲の動き
    # for b in range(6, 100):
    #    gen_s_a_b_c_image(a=5, b=b, c=100, len_Nz=len_Nz,
    #                      zoom=zoom, is_temporary=False)

    # 雲の動き
    # for b in range(6, 30):
    #    gen_s_a_b_c_image(a=5, b=b, c=30, len_Nz=len_Nz,
    #                      zoom=zoom, is_temporary=False)

    # gen_odds()
    # gen_3chord()

    # for a in range(4, 5):
    #    for b in range(a+1, a+6):
    #        for c in range(b+1, b+40):
    #            gen_s_a_b_c_image(a=a, b=b, c=c, len_Nz=len_Nz, zoom=zoom)


def gen_a3_b5_c11to13():
    """3,5,11～13 Clouds passer"""
    gen_s_a_b_c_image(a=3, b=5, c=11, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=3, b=5, c=12, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=3, b=5, c=13, len_Nz=len_Nz, zoom=zoom)


def gen_a_plus_b():
    """p=a+bシリーズ"""
    gen_s_a_b_c_image(a=1, b=2, c=4, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=1, b=2, c=8, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=1, b=2, c=10, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=1, b=4, c=16, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=1, b=4, c=24, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=1, b=4, c=36, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=1, b=6, c=36, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=1, b=6, c=90, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=2, b=3, c=12, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=2, b=3, c=18, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=2, b=3, c=27, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=2, b=3, c=33, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=2, b=3, c=42, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=2, b=4, c=8, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=2, b=4, c=16, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=2, b=5, c=9, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=2, b=9, c=31, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=3, b=5, c=45, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=3, b=5, c=60, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=3, b=7, c=63, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=4, b=5, c=40, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=4, b=9, c=10, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=5, b=10, c=100, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=7, b=8, c=112, len_Nz=len_Nz, zoom=zoom)


def gen_odds():
    """奇数シリーズ"""
    gen_s_a_b_c_image(a=1, b=3, c=5, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=3, b=7, c=9, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=3, b=13, c=15, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=5, b=7, c=13, len_Nz=len_Nz, zoom=zoom)
    gen_s_a_b_c_image(a=7, b=43, c=45, len_Nz=len_Nz, zoom=zoom)


def gen_3chord():
    """3和音シリーズ"""
    roots = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    is_temporary = False

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
        root = roots[ms]

        gen_s_a_b_c_image(a=1+ms, b=5+ms, c=8+ms,
                          len_Nz=len_Nz, zoom=zoom, suffix=f"{root}", is_temporary=is_temporary)
        """メジャーコード"""

        gen_s_a_b_c_image(a=1+ms, b=4+ms, c=8+ms,
                          len_Nz=len_Nz, zoom=zoom, suffix=f"{root}m", is_temporary=is_temporary)
        """m マイナーコード"""

        gen_s_a_b_c_image(a=1+ms, b=6+ms, c=8+ms,
                          len_Nz=len_Nz, zoom=zoom, suffix=f"{root}sus4", is_temporary=is_temporary)
        """sus4 サスフォー"""

        gen_s_a_b_c_image(a=1+ms, b=5+ms, c=7+ms,
                          len_Nz=len_Nz, zoom=zoom, suffix=f"{root}-5", is_temporary=is_temporary)
        """-5 フラットファイブ"""

        gen_s_a_b_c_image(a=1+ms, b=5+ms, c=9+ms,
                          len_Nz=len_Nz, zoom=zoom, suffix=f"{root}aug", is_temporary=is_temporary)
        """aug オーギュメント"""

        gen_s_a_b_c_image(a=1+ms, b=4+ms, c=7+ms,
                          len_Nz=len_Nz, zoom=zoom, suffix=f"{root}dim", is_temporary=is_temporary)
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

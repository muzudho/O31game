"""
pip install opencv-python
pip install Pillow

cd me

python.exe -m ideas.transfer_map_victory.main
"""
from ideas.transfer_map_victory.s_a_b_c_image_gen import gen_s_a_b_c_image

zoom = 0.8
"""倍率。1倍はかなりでかい"""


def main():
    gen_s_a_b_c_image(a=1, b=4, c=7, zoom=zoom)
    # gen_s_a_b_c_image(a=3, b=5, c=12, zoom=zoom)
    # gen_s_a_b_c_image(a=2, b=4, c=6, zoom=zoom)

    # gen_3chord()


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

        gen_s_a_b_c_image(a=1+ms, b=5+ms, c=8+ms,
                          zoom=zoom, is_temporary=False)
        """メジャーコード"""

        gen_s_a_b_c_image(a=1+ms, b=4+ms, c=8+ms,
                          zoom=zoom, is_temporary=False)
        """m マイナーコード"""

        gen_s_a_b_c_image(a=1+ms, b=6+ms, c=8+ms,
                          zoom=zoom, is_temporary=False)
        """sus4 サスフォー"""

        gen_s_a_b_c_image(a=1+ms, b=5+ms, c=7+ms,
                          zoom=zoom, is_temporary=False)
        """-5 フラットファイブ"""

        gen_s_a_b_c_image(a=1+ms, b=5+ms, c=9+ms,
                          zoom=zoom, is_temporary=False)
        """aug オーギュメント"""

        gen_s_a_b_c_image(a=1+ms, b=4+ms, c=7+ms,
                          zoom=zoom, is_temporary=False)
        """dim ディミニッシュ"""


if __name__ == "__main__":
    main()

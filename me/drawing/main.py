"""
pip install opencv-python

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

# 3和音シリーズ
gen_s_a_b_c_image(a=1, b=5, c=8, len_Nz=len_Nz, zoom=zoom)
"""C シーメジャーコード"""

gen_s_a_b_c_image(a=1, b=4, c=8, len_Nz=len_Nz, zoom=zoom)
"""Cm シーマイナーコード"""

gen_s_a_b_c_image(a=1, b=6, c=8, len_Nz=len_Nz, zoom=zoom)
"""Csus4 シーサスフォー"""

gen_s_a_b_c_image(a=1, b=5, c=7, len_Nz=len_Nz, zoom=zoom)
"""C-5 シーフラットファイブ"""

gen_s_a_b_c_image(a=1, b=5, c=9, len_Nz=len_Nz, zoom=zoom)
"""Caug シーオーギュメント"""

gen_s_a_b_c_image(a=1, b=4, c=7, len_Nz=len_Nz, zoom=zoom)
"""Cdim シーディミニッシュ"""

gen_s_a_b_c_image(a=2, b=6, c=9, len_Nz=len_Nz, zoom=zoom)
"""C# シーシャープメジャーコード"""

gen_s_a_b_c_image(a=2, b=5, c=9, len_Nz=len_Nz, zoom=zoom)
"""C#m シーシャープマイナーコード"""

gen_s_a_b_c_image(a=2, b=7, c=9, len_Nz=len_Nz, zoom=zoom)
"""C#sus4 シーシャープサスフォー"""

gen_s_a_b_c_image(a=2, b=6, c=8, len_Nz=len_Nz, zoom=zoom)
"""C#-5 シーシャープフラットファイブ"""

gen_s_a_b_c_image(a=2, b=6, c=10, len_Nz=len_Nz, zoom=zoom)
"""C#aug シーシャープオーギュメント"""

gen_s_a_b_c_image(a=2, b=5, c=8, len_Nz=len_Nz, zoom=zoom)
"""C#dim シーシャープディミニッシュ"""

gen_s_a_b_c_image(a=3, b=7, c=10, len_Nz=len_Nz, zoom=zoom)
"""D ディーメジャーコード"""

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

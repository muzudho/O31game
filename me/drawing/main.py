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
gen_s_a_b_c_image(a=4, b=9, c=19, len_Nz=len_Nz, zoom=zoom)

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

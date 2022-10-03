"""
pip install opencv-python

cd me

python.exe -m drawing.main
"""
import random
from drawing.s_a_b_c_image_gen import gen_s_a_b_c_image

len_Nz = 200
"""とりあえず c の２倍はある要素数。画像の横幅にも使われるので大きすぎないように
画像ファイルは、この半分ぐらいの部分で作ります"""

for i in range(0, 1):
    a = random.randint(1, 10)
    b = a + random.randint(1, 10)
    c = b + random.randint(1, 10)

    gen_s_a_b_c_image(a=a, b=b, c=c, len_Nz=len_Nz, zoom=0.4)

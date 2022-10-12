"""
pip install opencv-python
pip install Pillow

cd me

python.exe -m ideas.fixed_period.main
"""
import random
from ideas.fixed_period.s_a_b_c_p_image_gen import gen_s_a_b_c_p_image

zoom = 0.25
"""倍率。1倍はかなりでかい"""


def main():
    gen_s_a_b_c_p_image(S={1}, p=2,
                        zoom=1.0, is_temporary=False)

    gen_s_a_b_c_p_image(S={1, 2}, p=3,
                        zoom=1.0, is_temporary=False)

    gen_s_a_b_c_p_image(S={1, 2, 3}, p=4,
                        zoom=1.0, is_temporary=False)


if __name__ == "__main__":
    main()

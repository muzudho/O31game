"""
pip install opencv-python
pip install Pillow

cd me

python.exe -m ideas.vector_coordinate.main
"""
import cv2
import numpy as np
from ideas.vector_coordinate.s_a_b_c_image_gen import gen_s_a_b_c_image


def main():
    gen_s_a_b_c_image()


if __name__ == "__main__":
    main()

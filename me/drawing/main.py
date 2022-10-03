"""
cd me

python.exe -m drawing.main
"""
import cv2
import numpy as np
from datetime import datetime

# 描画する画像を作る,128を変えると色を変えれます 0黒→255白
canvas = np.full((250, 600, 3), 128, dtype=np.uint8)

# 線、描画する画像を指定、座標1点目、2点目、色、線の太さ
white = (255, 255, 255)
cv2.line(canvas, (120, 10), (220, 110), white, thickness=1)

date = datetime.now().strftime("%Y%m%d_%H%M%S")
cv2.imwrite(f"./output/{date}-tmp.png", canvas)

# マルチバイト文字対応
from PIL import ImageFont, ImageDraw, Image


def put_multibyte_char(canvas, text):
    fontpath = "./simsun.ttc"  # <== 这里是宋体路径
    font = ImageFont.truetype(fontpath, 32)
    img_pil = Image.fromarray(canvas)
    draw = ImageDraw.Draw(img_pil)
    b, g, r, a = 0, 255, 0, 0
    draw.text((50, 80),  text, font=font, fill=(b, g, r, a))
    canvas2 = np.array(img_pil)
    return canvas2

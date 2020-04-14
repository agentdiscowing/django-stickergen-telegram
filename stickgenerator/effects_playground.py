from PIL import Image, ImageDraw, ImageFont
from skimage import io, transform
import requests
from io import BytesIO


def reformat(path):
        pic = io.imread(path)
        try:
            path = path.replace("jpg", "png")
        except Exception:
            pass
        pic = transform.resize(pic, (512, 512), anti_aliasing=False)
        io.imsave(path, pic)
        return path


def bw_rainy(path : str):
    pic = io.imread(path, as_gray=True)
    io.imsave(path, pic)
    im = Image.open(path)
    response = requests.get("https://i.dlpng.com/static/png/6388472_preview.png")
    rain = Image.open(BytesIO(response.content))
    rain = rain.resize(im.size)
    im = im.convert(rain.mode)
    im = Image.blend(im, rain, 0.45)
    im.save(path)


def red_sunset(path: str):
    pic = io.imread(path)
    red_multiplier = [1, 0, 0]
    pic = pic * red_multiplier
    io.imsave(path, pic)


def fatal_windblow(path:str):
    pic = io.imread(path)
    pic = transform.swirl(pic, rotation=0, strength=6, radius=240)
    io.imsave(path, pic)

# pass color as (r, g, b)


def add_text(path: str, text: str, fontsize: int = 32, color: tuple = (0, 0, 0)):
    img = Image.open(path)
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype(r"D:\code\Python\stickgenerator\fonts\arial.ttf", fontsize)
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text(((512 - len(text) * fontsize / 2) / 2, 440), text, color, font=font)
    img.save(path)


path = r'D:\code\Python\baby_farrot.png'
add_text(path, "ах аставьте меня!!!")

from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance, ImageChops, ImageFilter
import requests
from io import BytesIO

def rainy(im):
    response = requests.get("https://media.istockphoto.com/photos/water-drops-rain-droplets-on-white-background-picture-id1044257942")
    rain = Image.open(BytesIO(response.content))
    rain = rain.resize(im.size)
    im = im.convert(rain.mode)
    im = Image.blend(im, rain, 0.35)
    return im


# def red_sunset(path: str):
#     pic = io.imread(path)
#     red_multiplier = [1, 0, 0]
#     pic = pic * red_multiplier
#     return pic


# def fatal_windblow(path: str):
#     pic = io.imread(path)
#     pic = transform.swirl(pic, rotation=0, strength=6, radius=240)
#     return pic

def black_white(image):
    """Change image to greyscale."""
    return ImageOps.grayscale(image)


def glassial_blur(image, amount=1):
    """Blur image."""
    im = image.filter(ImageFilter.GaussianBlur(radius=amount))
    return im


def desaturate(image, amount=.5):
    """Reduce vibrance."""
    enhanced = ImageEnhance.Color(image)
    return enhanced.enhance(amount)


def saturate(image, amount=1.5):
    """Increase vibrance."""
    enhanced = ImageEnhance.Color(image)
    return enhanced.enhance(amount)


def sharpness(image, amount=1.5):
    """Shapen edges of an image."""
    enhanced = ImageEnhance.Sharpness(image)
    return enhanced.enhance(amount)


def contrast(image, amount=1.5):
    """Adjust ."""
    enhanced = ImageEnhance.Contrast(image)
    return enhanced.enhance(amount)


def invert(image):
    """Invert the image."""
    return ImageChops.invert(image)


def flip(image):
    """Flip image."""
    return ImageOps.flip(image)


def mirror(image):
    """Mirrior image horizontally."""
    return ImageOps.mirror(image)


def rotate(image):
    """Rotate image by 90 degrees."""
    return image.rotate(90)


def reset(reseted_image_path, source_image_path):
    im = Image.open(source_image_path)
    im.save(reseted_image_path)

# pass color as (r, g, b)
# def add_text(img, text: str, fontsize: int = 32, color: tuple = (0, 0, 0)):
#     draw = ImageDraw.Draw(img)
#     # font = ImageFont.truetype(<font-file>, <font-size>)
#     font = ImageFont.truetype(r"D:\code\Python\stickgenerator\fonts\arial.ttf", fontsize)
#     # draw.text((x, y),"Sample Text",(r,g,b))
#     draw.text(((512 - len(text) * fontsize / 2) / 2, 440), text, color, font=font)
#     return img


def add_effect(applied_effect, path):
        img = Image.open(path)
        img = applied_effect(img)
        img.save(path)



# Create list  to handle respective effects
effect = {
    "Grayscale": black_white,
    "Blur": glassial_blur,
    "Desaturate": desaturate,
    "Saturate": saturate,
    "Sharpness": sharpness,
    "Contrast": contrast,
    "Invert": invert,
    "Flip": flip,
    "Mirror": mirror,
    "Rotate": rotate,
    "Rainy": rainy,
}




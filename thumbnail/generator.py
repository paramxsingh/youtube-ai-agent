# Placeholder for thumbnail generation
from PIL import Image, ImageDraw, ImageFont

def generate_thumbnail(text):
    img = Image.new('RGB', (1280, 720), color = (73, 109, 137))
    d = ImageDraw.Draw(img)
    d.text((10,10), text, fill=(255,255,0))
    path = 'thumbnails/thumb.jpg'
    img.save(path)
    return path
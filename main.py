from PIL import Image, ImageDraw, ImageFont


def make_meme(fp, top_text, bottom_text):
    image = Image.open(fp)
    w, h = image.size
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("impact.ttf", size=70)

    bbox_top = draw.textbbox((0, 0), top_text, font=font)
    bbox_bot = draw.textbbox((0, 0), bottom_text, font=font)

    draw.text(((w - bbox_top[2]) // 2, 0), top_text, font=font, stroke_fill="black", stroke_width=4)
    draw.text(((w - bbox_bot[2]) // 2, h - bbox_bot[3] - 10), bottom_text, font=font, stroke_fill="black",
              stroke_width=4)

    image.save("meme.png")


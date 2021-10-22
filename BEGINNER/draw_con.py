from PIL import Image, ImageDraw, ImageFont
import solve_tools

SHUFFEL = solve_tools.SHUFFEL.copy()

im = Image.new("RGB", (1280, 640), (0x0, 0x0, 0x0))
draw = ImageDraw.Draw(im)
font = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans.ttf", 20)

HIGH_VERT = 60
HIGH_MESH = 400

correct = [True, True, True, True,     True, False, True, True,     True, True, True, False,     True, True, True, True]

for i in range(1, 5):
    draw.line([(i*320, 0), (i*320, 640)], width=2, fill=(255, 0, 255))

for i in range(16):
    dest = SHUFFEL[i] & 0b1111
    
    if correct[dest]:
        text_color_dest = (0, 255, 0)
    else:
        text_color_dest = (255, 255, 255)

    if correct[i]:
        text_color = (0, 255, 0)
    elif correct[dest]:
        text_color = (255, 255, 0)
    else:
        text_color = (255, 255, 255)



    draw.text((40 + 80*i, 10), "{:1X}".format(i), font=font, align="left", fill=text_color) 
    draw.text((40 + 80*i, 40 + 2*HIGH_VERT + HIGH_MESH), "{:1X}'".format(dest), font=font, align="left", fill=text_color_dest)
    draw.line([(46 + 80*i, 35), (46 + 80*i, 35 + HIGH_VERT)])
    draw.line([(46 + 80*i, 35 + HIGH_VERT + HIGH_MESH), (46 + 80*i, 35 + 2*HIGH_VERT + HIGH_MESH)])
    draw.line([(46 + 80*i, 35 + HIGH_VERT + HIGH_MESH), (46 + 80*dest, 35 + HIGH_VERT)])

im.show()
im.save("shuffel.png")

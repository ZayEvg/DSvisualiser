from tkinter import *
import re
from PIL import Image, ImageDraw

root = Tk()
canv = Canvas(root, width=540, height=960)
canv.pack()

image1 = Image.new('RGB', (540, 960), (255, 255, 255))
draw = ImageDraw.Draw(image1)

dataset = ''
with open('DS5.txt', 'r') as input_file:
    dataset = input_file.read()

dataset = re.findall('(\d{2,3}\s\d{2,3})\n', dataset)
x = 0
y = 0
for el in dataset:
    x = int(re.findall('(\d{2,3})\s\d{2,3}', el)[0])
    y = int(re.findall('\d{2,3}\s(\d{2,3})', el)[0])
    canv.create_line(x, y, x+1, y+1)
    draw.line((x, y, x+1, y+1), fill=256)
image1.save('result.jpg')

root.mainloop()

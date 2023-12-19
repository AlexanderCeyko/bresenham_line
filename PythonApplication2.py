from PIL import Image

def ALG_bresenham(x1, y1, x2, y2):
    image = Image.new('RGB',(1000,1000))
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    if x1 < x2:
        sx = 1  
    else: 
        sx = -1

    if y1 < y2:
       sy = 1 
    else:
       sy = -1

    x, y = x1, y1

    epsilon = dx - dy

    while True:
        image.putpixel((x,y),100)
        if x == x2 and y == y2:
            break
        e2 = 2 * epsilon
        if e2 > -dy:
            epsilon -= dy
            x += sx
        if e2 < dx:
            epsilon += dx
            y += sy
    image.show()

x1, y1 = 935,427
x2, y2 = 300,650

ALG_bresenham(x1, y1, x2, y2)
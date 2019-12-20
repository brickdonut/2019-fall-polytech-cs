def setup():
    size(500,500)
    smooth()
    background(120)
    strokeWeight(1)
    
counter = 0
counter1 = 0
nx = 0
ny = 0
cx = 250
cy = 250
R = 10
switcher = 1


def draw():
    global counter1, nx, ny, cx, cy, R, switcher, counter
    if switcher > 0:
        nx = cos(counter1)*R + cx
        ny = sin(counter1)*R +cy
        stroke(0,50)
    else:
        nx = sin(counter1)*R+cx
        ny = cos(counter1)*R+cy
        stroke(250,50)
        
    switcher *=-1
    
    x1 = nx - sin(counter)*30
    y1 = ny - cos(counter)*30
    x2 = nx + sin(counter)*30
    y2 = ny + cos(counter)*30
    
    line(x1, y1, x2, y2)
    
    counter +=0.1
    if counter > 2*PI:
        counter = 0
    
    counter1 +=0.01
    R += counter / 50
    if counter1 > 2*PI:
        counter1 = 0

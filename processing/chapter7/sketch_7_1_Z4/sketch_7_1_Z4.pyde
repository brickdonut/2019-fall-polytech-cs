def setup():
    size(500,500)
    smooth()
    background(255)
    strokeWeight(1)
    
counter = 0
counter1 = 0
cx = 250
cy = 250
R = 10

def draw():
    global counter1, cx, cy, R, counter
    
    stroke(0,50)
    
    nx = sin(counter1)*R + cx
    ny = cos(counter1)*R + cy
    
    x1 = nx - sin(counter)*100
    y1 = ny - cos(counter)*100
    x2 = nx + sin(counter)*100
    y2 = ny + cos(counter)*100
    
    fill(random(0,255), random(0,255),random(0,255), 100)
    
    ellipse(x1, y1, x2/3, y2/3)
    
    counter +=0.1
    if counter > 2*PI:
        counter = 0
    
    counter1 +=0.01
    R += counter / 50
    if counter1 > 2*PI:
        counter1 = 0

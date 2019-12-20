
def setup():
    size(500,500)
    smooth()
    background(0)
    strokeWeight(1)
    
    
counter = 1
cx=250
cy=250
nx = 0
ny = 0
counter1 = 1
R = 20
ncx = 1
ncy = 1 

def oneLineDraw(ncx, ncy):
    global cx,counter,cy,nx,ny,counter1,R
    x1 = ncx - sin(counter1)*100
    y1 = ncy - cos(counter1)*100
    x2 = ncx + sin(counter1)*100
    y2 = ncy + cos(counter1)*100
    line(x1,y1,x2,y2)
    
def draw():
    global cx,counter,cy,nx,ny,counter1,R, ncx, ncy
    stroke(200,25)
    nx = sin(counter1)*R + cx
    ny = cos(counter1)*R + cy
    
    x1 = nx - sin(counter)*150
    y1 = ny - cos(counter)*150
    x2 = nx + sin(counter)*150
    y2 = ny + cos(counter)*150
    
    oneLineDraw(x2,y2)
    oneLineDraw(x1,y1)
    
    counter += 0.1
    if counter > 2*PI:
        counter = 0
        
    counter1 += 0.01
    R += counter/20
    if counter1 > 2*PI:
        counter1 = 0

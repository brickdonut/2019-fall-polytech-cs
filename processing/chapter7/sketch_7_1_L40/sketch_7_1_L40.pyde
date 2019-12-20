def setup():
    size(500,500)
    smooth()
    background(50)
    strokeWeight(2)
    stroke(250)

counter= 0
mcolor=0
cx = 250
cy = 250
R = 200


def draw():
        global cx,cy, R, counter, mcolor
        y1 = cos(counter)*R + cy
        x1 = sin(counter)*R + cx
        mcolor=mcolor+1
        stroke(mcolor)
        line(cx,cy,x1,y1)
        counter=counter+2*PI/255
        while counter> 2*PI:
         counter= 0
         mcolor=0
         background(50)
        
def keyPressed():
    if key =="s":
        saveFrame("mP")

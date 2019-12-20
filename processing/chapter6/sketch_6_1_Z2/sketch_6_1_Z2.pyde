def setup():
    size(500,500)
    smooth()
    strokeWeight(1)
    background(0)

i = 0
k = 1
flug = 1
myY1 = 0
myY2 = 0

def upDate():
    global i, k, flug, myY1, myY2
    i +=k
    if i == 255:
        k=-1
    if i == 0:
        k=1    

def draw():
    global i, k, flug, myY1, myY2
    stroke(i,20)
    myY1 = mouseY -  random(-80,80)
    myY2 = mouseY +  random(-80,80)
    line(0,myY1,500, myY2)
    upDate()

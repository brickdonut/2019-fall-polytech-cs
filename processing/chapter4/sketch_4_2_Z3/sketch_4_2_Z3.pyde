def setup():
    size (600,600)
    noLoop()
       
def drawMyScene(myColor,x):
    rotate(PI/4*x)
    fill(myColor)
    rect(0,50,150,50)
    rect(50,0,50,150)
    
def draw():
    background(20)
    smooth()
    noStroke()
    
    pushMatrix()
    translate(100,0)
    drawMyScene(180,1)
    popMatrix()
    
    pushMatrix()
    translate(420,150)
    scale(2)
    drawMyScene(220,2)
    popMatrix()    
    
    pushMatrix()
    translate(480,330)
    scale(1.4)
    drawMyScene(80,1)
    popMatrix()        

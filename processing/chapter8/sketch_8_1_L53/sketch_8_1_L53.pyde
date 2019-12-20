counter = 0
cx = 0
cy = 0
fsize = 0

class FunnyRect():

    def setCenter(self, x,y):
        self.cx = x
        self.cy = y

    def setSize(self, size):
        self.size = size

    def render(self):
        rect(self.cx, self.cy, self.size, self.size)


funnyRect = FunnyRect()
funnyRect1 = FunnyRect()

def setup():
    size(600,600)
    smooth()
    noStroke()
    rectMode(CENTER)
    funnyRect.setSize(50)
    funnyRect1.setSize(20)

def draw():
    background(255)
    fill(50)
    global counter
    
    objX = mouseX +sin(counter)*150
    objY = mouseY +cos(counter)*150
    
    funnyRect.setCenter(mouseX, mouseY)
    funnyRect.render()
    
    funnyRect1.setCenter(objX, objY)
    funnyRect1.render()
    counter +=0.05

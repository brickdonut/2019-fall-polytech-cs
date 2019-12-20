radius = 50
centerX = 500/2
centerY = 500/2
leng = 350
angle = PI/4
weight = 1
counter = 0
a = 0
b = 0
c = 0
class myline():
    
    def render(self, centerX, centerY, angle):
        x1 = centerX - cos(angle)*leng/2
        y1 = centerY + sin(angle)*leng/2
        x2 = centerX + cos(angle)*leng/2
        y2 = centerY - sin(angle)*leng/2
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
                
        stroke(150,100)
        strokeWeight(weight)
        line(x1,y1,x2,y2)
        
    def colors(self):
        global a, b, c
        a += random(0,10)
        b += random(0,5)
        c += random(10,15)
        
        if a >200:
            a = -a
        if b > 200:
            b =-b
        if c >200:
            c = -c
            
        stroke( a, b, c, 300)
        strokeWeight(10)
        line(self.x2, self.y2, self.x2, self.y2)
        line(self.x1, self.y1, self.x1, self.y1)

myline = myline()

def setup():
    size(500,500)
    smooth()
    background(0)
    
    
def colorS():
    global a, b, c

    
    
def draw():
    global counter, radius
    counter += 0.05
    
    if counter > 2*PI:
        counter = 0
        radius += 50
    centerX = width/2 + sin(counter)*radius
    centerY = width/2 + cos(counter)*radius
    angle = counter*2

    myline.render(centerX, centerY, angle)
    myline.colors()

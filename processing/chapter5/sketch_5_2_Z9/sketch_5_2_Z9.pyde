def setup():
   size(500,500)
   smooth()
   noLoop()
   noStroke()
   ellipseMode(CENTER)



def draw():
   background(255)
   border = 50
   nw = width-2*border
   nh = height-2*border
   number = 5
   nWstep = nw / number
   nHstep = nh / number
   i = 0
   j = 0
   k = 0
   h = 0
   while i < number:
    while j < number:
        x = border + j*nWstep + nWstep/2
        y = border + i*nHstep + nHstep/2
        size =95 - (k+1)*10
        mColor = size*1.5
        fill(mColor, 10, 190)
        ellipse(x, y, size, size)
        fill(250)
        ellipse(x,y,3,3)
        j=j+1
        k = k+1
    i = i+1
    h =h+0.75
    k = 0 + h
    j = 0    

def setup():
  size(500,500)
  smooth()
  background(255)
  strokeWeight(30)
  noLoop()
  
def draw():
  stroke(20)
  line(50,200,150,300)
  line(50*2,200,150+50,300)
  line(50*3,200,150+50*2,300)
  line(50*4,200,150+50*3,300)
  line(50*5,200,150+50*4,300)
  line(50*6,200,150+50*5,300)
  line(50*7,200,150+50*6,300)

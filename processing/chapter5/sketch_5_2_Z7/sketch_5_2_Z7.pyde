def setup():
  size(500,500)
  smooth()
  background(255)
  strokeWeight(30)
  noLoop()
  
def draw():
    k = 1;
    i = 1;
    while k < 4:    
      while i < 8:
        stroke(20*i) 
        line(i*50, 100*k, 150 + (i-1)*50, 100+100*k)
        stroke(160-20*i)
        line(i*50+100, 100*k, 50 + (i-1)*50, 100+100*k)
        i = i+1
      i=1
      k = k+1
    

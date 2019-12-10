def setup():
  size(500,500)
  smooth()
  background(255)
  strokeWeight(30)
  noStroke(); 
  noLoop()
  
def draw():
    k = 0;
    while k < 10:   
        fill(k*20)
        rect(k*40+50, 220, 35, 35)
        k=k+1

       
    

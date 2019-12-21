add_library('sound')
amount = 20
num=0.05
scale = 2.0
bands = 64
sum = [0.0] * bands
smooth_factor = 0.02

def setup():
    fullScreen()
    stroke(255)
    size(900, 500)
    smooth()
    global img,img1
    img = loadImage("rfcc.jpg")
    img1 = loadImage("cs.png")
    imageMode(CENTER)
    
    sample = SoundFile(this, "md1.mp3")
    sample.loop()
 
    global fft
    fft = FFT(this, bands)
    fft.input(sample)
    
class casset():
  def render(self):
        global num
        image(img, width / 2, height / 2)
        translate(width/2, height/2)
        for i, v in enumerate(sum):
           sum[i] += (fft.spectrum[i] - v) * smooth_factor
           fill(random(150,200), random(50,100),0 ,200) 
           ellipse(250,-35, (-sum[i] * height * scale)*1.5, (-sum[i] * height * scale)*1.5)
           ellipse(-250,-35, (-sum[i] * height * scale)*1.5,  (-sum[i] * height * scale)*1.5)
           num += 0.01
           pushMatrix()
           translate(250,-35)
           rotate(frameCount)
           image(img1,0,0)
           popMatrix()
           pushMatrix()
           translate(-250,-35)
           rotate(frameCount)
           image(img1,0,0)
           popMatrix()
        
cass=casset()

def draw():
   background(88,40,30)
   fft.analyze()
   cass.render()

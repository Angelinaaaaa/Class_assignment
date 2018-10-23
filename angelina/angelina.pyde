x=0
y=300

def setup():
    size(640, 480)

def draw():
    global x
    global y
    
    if x >= 640:
        x = 0
    x+=3
    
    if y >= 640:
        y = 0
    y+=2
    
    background(135,206,250)
    
    noStroke()
    fill(250,250,250)
    ellipse(x+40, height/3, 50, 50)
    ellipse(x+45, height/3-40, 50, 50)
    ellipse(x+70,height/3-20, 50, 50)
    ellipse(x+20,height/3-15, 50, 50)
    ellipse(x-10,height/3-10, 50, 50)
  

    ellipse(y+40, height/3-40, 50, 50)
    ellipse(y+45, height/3-80, 50, 50)
    ellipse(y+70,height/3-60, 50, 50)
    ellipse(y+20,height/3-55, 50, 50)
    ellipse(y-10,height/3-50, 50, 50)

    
    fill(0,128,0)
    rect(0,350,700,250)
    
    fill(65,105,225)
    ellipse(120,400,200,40)
    
    fill(205,133,63)
    rect(210,320,180,120)
    
    fill(255,99,71)
    triangle(150,360,300,260,450,360)
    
    fill(205,133,63)
    rect(460,340,70,40)
    
    fill(255,99,71)
    triangle(435,340,495,300,555,340)
    

    

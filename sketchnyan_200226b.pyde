#MOUSE PROCESSOR
#MAY BELLEN PALENCIA BSCS 1-A

nyanX=50
nyanY=50

def setup():
    size(1000, 800);
    background(400);    
def draw():
    frameRate(20)
    background(35, 35, 109)
    fill(255, 255, 198)
    ellipse(random(width), random (height), 10, 10)
    fill(500, 550, 575)
    ellipse(random(800), random (800), 10, 10)
    fill(300, 150, 300)
    ellipse(random(800), random (800), 10, 10)
    noStroke()
    rainbow1()
    body()
    face()
    eyes()
    nose()
    mouth()
    cheeks()
    feet()
    tail()
    stars()
def rainbow1():
    for i in range(6):
      noStroke();
      fill((128), (0), (255));
      rect(mouseX+200, mouseY+500, 50, 20); 
      fill((0), (0), (255));
      rect(mouseX+200, mouseY+480, 50, 20);
      fill((0), (255), (0));
      rect(mouseX+200, mouseY+460, 50, 20);
      fill((255), (255), (0));
      rect(mouseX+200, mouseY+440, 50, 20);
      fill((255), (128), (0));
      rect(mouseX+200, mouseY+420, 50, 20);
      fill((255), (0), (0));
      rect(mouseX+200, mouseY+400, 50, 20);
    for i in range(6):
      noStroke();
      fill((128), (0), (255));
      rect(mouseX+250, mouseY+490, 70, 20); 
      fill((0), (0), (255));
      rect(mouseX+250, mouseY+470, 70, 20);
      fill((0), (255), (0));
      rect(mouseX+250, mouseY+450, 70, 20);
      fill((255), (255), (0));
      rect(mouseX+250, mouseY+430, 70, 20);
      fill((255), (128), (0));
      rect(mouseX+250, mouseY+410, 70, 20);
      fill((255), (0), (0));
      rect(mouseX+250, mouseY+390, 70, 20);
    for i in range(6):
      noStroke();
      fill((128), (0), (255));
      rect(mouseX+320, mouseY+500, 50, 20); 
      fill((0), (0), (255));
      rect(mouseX+320, mouseY+480, 50, 20);
      fill((0), (255), (0));
      rect(mouseX+320, mouseY+460, 50, 20);
      fill((255), (255), (0));
      rect(mouseX+320, mouseY+440, 50, 20);
      fill((255), (128), (0));
      rect(mouseX+320, mouseY+420, 50, 20);
      fill((255), (0), (0));
      rect(mouseX+320, mouseY+400, 50, 20);
    for i in range(6):
      noStroke();
      fill((128), (0), (255));
      rect(mouseX+370, mouseY+490, 70, 20); 
      fill((0), (0), (255));
      rect(mouseX+370, mouseY+470, 70, 20);
      fill((0), (255), (0));
      rect(mouseX+370, mouseY+450, 70, 20);
      fill((255), (255), (0));
      rect(mouseX+370, mouseY+430, 70, 20);
      fill((255), (128), (0));
      rect(mouseX+370, mouseY+410, 70, 20);
      fill((255), (0), (0));
      rect(mouseX+370, mouseY+390, 70, 20);    
def body():
    for i in range(1):
        #black
      fill((0), (0), (0))
      rect(mouseX+445, mouseY+380, 140, 10);
      rect(mouseX+430, mouseY+390, 170, 100);
      rect(mouseX+445, mouseY+490, 140, 10);
      #cream
      fill((239), (228), (176))
      rect(mouseX+440, mouseY+390, 150, 10);
      rect(mouseX+440, mouseY+400, 150, 90); 
      #small black squares at the edge
      fill((0), (0), (0))
      square(mouseX+435, mouseY+385, 10)     
      square(mouseX+435, mouseY+485, 10)
      square(mouseX+585, mouseY+385, 10)    
      square(mouseX+585, mouseY+485, 10)    
      #violet
      fill((255), (128), (255))
      rect(mouseX+465, mouseY+395, 100, 10)
      rect(mouseX+450, mouseY+405, 130, 70)
      rect(mouseX+465, mouseY+475, 100, 10)
      #small squares at the edge
      fill((255), (128), (255))
      square(mouseX+455, mouseY+400, 10)         
      square(mouseX+455, mouseY+470, 10)  
      square(mouseX+565, mouseY+400, 10) 
      square(mouseX+565, mouseY+470, 10) 
      #small squares inside the box
      fill((215), (0), (215))
      square(mouseX+490, mouseY+420, 7)
      square(mouseX+455, mouseY+420, 7)
      square(mouseX+460, mouseY+440, 7)
      square(mouseX+490, mouseY+445, 7)
      square(mouseX+480, mouseY+470, 7)
      square(mouseX+500, mouseY+400, 7)
      square(mouseX+520, mouseY+470, 7)
      square(mouseX+550, mouseY+450, 7)
      square(mouseX+530, mouseY+420, 7)
      square(mouseX+560, mouseY+410, 7)
      square(mouseX+560, mouseY+410, 7)
def face():
      fill((0), (0), (0))
      rect(mouseX+535, mouseY+425, 20, 10)
      rect(mouseX+530, mouseY+430, 10, 20)
      rect(mouseX+525, mouseY+450, 10, 30)
      rect(mouseX+555, mouseY+490, 90, 10)
      square(mouseX+535, mouseY+480, 7)
      square(mouseX+540, mouseY+485, 7)
      rect(mouseX+635, mouseY+450, 30, 30)
      rect(mouseX+640, mouseY+433, 20, 20)
      rect(mouseX+635, mouseY+425, 20, 10)
      # fill((300), (300), (300))
      square(mouseX+630, mouseY+433, 10)
      square(mouseX+625, mouseY+440, 10)
      #gray square
      fill((150), (150), (150))
      square(mouseX+540, mouseY+435, 20)
      square(mouseX+555, mouseY+440, 7)
      rect(mouseX+535, mouseY+445, 123, 35)
      square(mouseX+635, mouseY+435, 20)
      rect(mouseX+542, mouseY+480, 110, 6)
      rect(mouseX+547, mouseY+485, 100, 6)
      #small squares
      fill((0), (0), (0))
      square(mouseX+555, mouseY+435, 7)
      square(mouseX+560, mouseY+440, 7)
      rect(mouseX+560, mouseY+445, 70, 5)
      square(mouseX+650, mouseY+480, 7)
      square(mouseX+645, mouseY+485, 7)
def eyes():
      fill((0), (0), (0))
      square(mouseX+560, mouseY+455, 15)
      square(mouseX+615, mouseY+455, 15)
def nose():
      square(mouseX+595, mouseY+460, 7)
      fill((255), (255), (255))     
      square(mouseX+560, mouseY+455, 7)
      square(mouseX+615, mouseY+455, 7)
def mouth():
      fill((0), (0), (0))
      rect(mouseX+565, mouseY+480, 60, 7)
      square(mouseX+565, mouseY+475, 7)
      square(mouseX+593, mouseY+475, 7)
      square(mouseX+618, mouseY+475, 7)
def cheeks():
      fill((255), (145), (145))
      square(mouseX+540, mouseY+460, 15)
      square(mouseX+638, mouseY+460, 15)
def feet():
      fill((150), (150), (150))
      square(mouseX+560, mouseY+500, 10)
      square(mouseX+615, mouseY+500, 10)
      square(mouseX+480, mouseY+500, 10)
      square(mouseX+420, mouseY+490, 25)
      fill((0), (0), (0))
      square(mouseX+553, mouseY+500, 8)
      square(mouseX+568, mouseY+500, 10)
      rect(mouseX+560, mouseY+510, 18, 7)
      square(mouseX+607, mouseY+500, 9)
      square(mouseX+625, mouseY+500, 9)
      rect(mouseX+615, mouseY+510, 10, 9)
      square(mouseX+470, mouseY+500, 10)
      rect(mouseX+470, mouseY+510, 20, 7)
      square(mouseX+490, mouseY+500, 9)
      rect(mouseX+420, mouseY+485, 10, 10)
      rect(mouseX+410, mouseY+490, 10, 20)
      rect(mouseX+420, mouseY+510, 20, 10)
      square(mouseX+440, mouseY+505, 10)
      square(mouseX+445, mouseY+500, 10)
def tail():
      fill((0), (0), (0))
      rect(mouseX+370, mouseY+430, 40, 10)
      rect(mouseX+370, mouseY+440, 10, 10)
      rect(mouseX+380, mouseY+448, 10, 10)
      rect(mouseX+390, mouseY+453, 10, 10)
      rect(mouseX+400, mouseY+458, 10, 10)
      rect(mouseX+410, mouseY+466, 20, 10)
      rect(mouseX+405, mouseY+435, 10, 10)
      rect(mouseX+410, mouseY+443, 10, 10)
      rect(mouseX+420, mouseY+448, 10, 10)
      fill((150), (150), (150))
      rect(mouseX+380, mouseY+440, 30, 10)
      rect(mouseX+390, mouseY+448, 20, 5)
      rect(mouseX+400, mouseY+450, 20, 8)
      rect(mouseX+410, mouseY+453, 20, 13)
def stars():
      fill((255), (255), (255))
      square(100, 300, 10)
      square(130, 500, 10)
      square(170, 900, 10)
      square(190, 400, 10)
      
      square(310, 290, 10)
      square(300, 300, 10)
      square(320, 300, 10)
      square(310, 310, 10)
     
      square(540, 140, 10)
      square(510, 170, 10)
      square(570, 170, 10)
      square(540, 200, 10)
      
      square(430, 550, 7)  
      square(400, 530, 7)  
      square(370, 550, 7)  
      square(+400, 570, 7)  
      
      square(610, 290, 7)
      square(600, 300, 7)
      square(620, 300, 7)
      square(610, 310, 7)
      

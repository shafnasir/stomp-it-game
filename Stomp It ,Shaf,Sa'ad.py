# Shaf Nasir,Saad Belim
# June 4,2014
# Stomp It Game

from graphics import*
from time import*
from random import*
# Shaf Nasir
win = GraphWin('Stomp It',800,500)

ground = Rectangle(Point(0,400),Point(800,500))
ground.setFill('Lawn Green')
ground.draw(win)

road = Rectangle(Point(0,400),Point(800,380))
road.setFill('Dim grey')
road.draw(win)

sky = Rectangle(Point(0,380),Point(800,0))
sky.setFill('Deep Sky Blue')
sky.draw(win)

cloud = Oval(Point(350,30),Point(230,70))
cloud.setFill('White Smoke')
cloud.draw(win)

cloud2 = Oval(Point(330,50),Point(220,80))
cloud2.setFill('White Smoke')
cloud2.draw(win)

cloud3 = Oval(Point(300,30),Point(210,70))
cloud3.setFill('White Smoke')
cloud3.draw(win)

cloud4 = Oval(Point(275,50),Point(200,80))
cloud4.setFill('White Smoke')
cloud4.draw(win)

cloud = Oval(Point(550,30),Point(430,70))
cloud.setFill('White Smoke')
cloud.draw(win)

cloud2 = Oval(Point(530,50),Point(420,80))
cloud2.setFill('White Smoke')
cloud2.draw(win)

cloud3 = Oval(Point(500,30),Point(410,70))
cloud3.setFill('White Smoke')
cloud3.draw(win)

cloud4 = Oval(Point(475,50),Point(400,80))
cloud4.setFill('White Smoke')
cloud4.draw(win)



xc = 290
yc = 350
dxc = 400
dyc = 320


car = Rectangle(Point(xc,yc),Point(dxc,dyc))
car.setFill('orangered')
car.draw(win)

wind = Rectangle(Point(292,300),Point(370,320))
wind.setFill('White')
wind.draw(win)

head = Circle(Point(350,310),10)
head.setFill('peru')
head.draw(win)

wheel = Circle(Point(305,365),20)
wheel.setFill('Black')
wheel.draw(win)

rim = Circle(Point(305,365),10)
rim.setFill('Light Grey')
rim.draw(win)

wheel2 = Circle(Point(380,365),20)
wheel2.setFill('Black')
wheel2.draw(win)

rim2 = Circle(Point(380,365),10)
rim2.setFill('Light Grey')
rim2.draw(win)

start = Rectangle(Point(200,180),Point(350,220))
start.setFill('chocolate')
start.draw(win)

exitb = Rectangle(Point(420,180),Point(570,220))
exitb.setFill('chocolate')
exitb.draw(win)

title = Rectangle(Point(250,20),Point(570,80))
title.setFill('chocolate')
title.draw(win)

startlabel = Text(Point(275,200),'Start')
startlabel.setFill('lawngreen')
startlabel.setSize(25)
startlabel.setStyle('bold italic')
startlabel.draw(win)

exitlabel = Text(Point(495,200),'Exit')
exitlabel.setFill('lawngreen')
exitlabel.setSize(25)
exitlabel.setStyle('bold italic')
exitlabel.draw(win)

title = Text(Point(400,50),'Stomp It')
title.setOutline('black')
title.setFill('Lawngreen')
title.setSize(36)
title.setFace('arial') 
title.setStyle('bold italic')
title.draw(win)


startlabel = win.getMouse()


        

win = GraphWin('Stomp It',800,450)



sky = Rectangle(Point(0,380),Point(800,0))
sky.setFill('Deep Sky Blue')
sky.draw(win)

ground = Rectangle(Point(0,350),Point(800,500))
ground.setFill('Lawn Green')
ground.draw(win)

road = Rectangle(Point(0,370),Point(800,330))
road.setFill('Dim grey')
road.draw(win)

cloud = Oval(Point(350,30),Point(230,70))
cloud.setFill('White Smoke')
cloud.draw(win)

cloud2 = Oval(Point(330,50),Point(220,80))
cloud2.setFill('White Smoke')
cloud2.draw(win)

cloud3 = Oval(Point(300,30),Point(210,70))
cloud3.setFill('White Smoke')
cloud3.draw(win)

cloud4 = Oval(Point(275,50),Point(200,80))
cloud4.setFill('White Smoke')
cloud4.draw(win)

cloud = Oval(Point(550,30),Point(430,70))
cloud.setFill('White Smoke')
cloud.draw(win)

cloud2 = Oval(Point(530,50),Point(420,80))
cloud2.setFill('White Smoke')
cloud2.draw(win)

cloud3 = Oval(Point(500,30),Point(410,70))
cloud3.setFill('White Smoke')
cloud3.draw(win)

cloud4 = Oval(Point(475,50),Point(400,80))
cloud4.setFill('White Smoke')
cloud4.draw(win)



xc = 290
yc = 350
dxc = 400
dyc = 320
midcar = 355
ycar = 335


car = Rectangle(Point(xc,yc),Point(dxc,dyc))
car.setFill('orangered')
car.draw(win)

wind = Rectangle(Point(292,300),Point(370,320))
wind.setFill('White')
wind.draw(win)

head = Circle(Point(350,310),10)
head.setFill('peru')
head.draw(win)

wheel = Circle(Point(305,365),20)
wheel.setFill('Black')
wheel.draw(win)

rim = Circle(Point(305,365),10)
rim.setFill('Light Grey')
rim.draw(win)

wheel2 = Circle(Point(380,365),20)
wheel2.setFill('Black')
wheel2.draw(win)

rim2 = Circle(Point(380,365),10)
rim2.setFill('Light Grey')
rim2.draw(win)



finish = True
g = 10
u = -100
x = 0
ctr = 0
ctr2 = 0
y = 290
y2 = 400
points = 0

finish == True

Points = Text(Point(400,400),points)
Points.setSize(36)
Points.setFill('black')
Points.undraw
Points.draw(win)

x1 = randint(500,800)
y1 = randint(200, 380)
obstacle= Rectangle(Point(x1, y1),Point(x1+80, y1-50))
obstacle.setFill("Chocolate")
obstacle.draw(win)

x1c = randint(0,800)
y1c = randint(0, 300)
coins = Circle(Point(x1c,y1c),12)
coins.setFill('yellow')
coins.draw(win)

while finish == True:
    if win.checkMouse() != None:
        car.move(x,u)
        wind.move(x,u)
        head.move(x,u)
        wheel.move(x,u)
        wheel2.move(x,u)
        rim.move(x,u)
        rim2.move(x,u)
        ycar = ycar+u
        ctr = ctr + 1
        sleep(0.02)
        if ctr == 1:
            u = u * 1.2
            ctr2 = 0
        else:
            u = -100
            
    elif ycar<290:
        car.move(0,g)
        wind.move(0,g)
        head.move(0,g)
        wheel.move(0,g)
        wheel2.move(0,g)
        rim.move(0,g)
        rim2.move(0,g)
        ycar = ycar+g
        sleep(0.02)
        ctr2 = ctr2 + 1
        u = -100
        if ctr2 > 1:
            g = g * 1.1
            ctr = 0
        else:
            g = 10
    if ycar <= 25 or ycar >= 300:
        car.move(0,0)
        wind.move(0,0)
        head.move(0,0)
        wheel.move(0,0)
        wheel2.move(0,0)
        rim.move(0,0)
        rim2.move(0,0)

    sleep (0.01)
    obstacle.undraw()
    coins.undraw()
    obstacle.move(-7,0)
    coins.move(-7,0)
    obstacle.draw(win)
    coins.draw(win)
    
    
   
    x1 = x1 - 7
    x1c = x1c - 7


    if x1 <= -120:
        x1 = 800
        x1c = 800
        
        y1 = randint(200, 300)
        y1c = randint(0, 200)
        
     
        obstacle= Rectangle(Point(x1, y1),Point(x1+80, y1-50))
        obstacle.setFill("Chocolate")
        obstacle.draw(win)
        
        coins = Circle(Point(x1c,y1c),12)
        coins.setFill('yellow')
        coins.draw(win)
       
        
    if x1 <= 400 and x1>= 290 or x1 <=355 and x1 >= 290:
        if ycar <= y1+15 and ycar >= y1 -15 :
            Gameover = Text(Point(400,20),'Game Over!')
            Gameover.setSize(36)
            Gameover.setStyle('bold italic')
            Gameover.setFill('black')
            Gameover.draw(win)
            Playagain = Text(Point(400,100),'Double click anywhere to play again')
            Playagain.setFill('black')
            Playagain.draw(win)
            finish = False
            win.getMouse()
            Gameover.undraw()
            Playagain.undraw()
            obstacle.undraw()
            coins.undraw()
            Points.undraw()
            points = points - points
            u = -500
            finish = True
        
    if x1c <= 400 and x1c >= 290 or x1c <= 355 and x1c >= 290:
        if ycar <= y1c +5 and ycar >= y1c -5:
            Points.undraw()
            points = points + 10
            Points = Text(Point(400,400),points)
            Points.setSize(36)
            Points.setFill('black')
            Points.draw(win)
            coins.setFill('deep sky blue')
            coins.setOutline('deep sky blue')
            
            
            
    if points >= 100:
        Points.setFill('red')
        Points.setSize(36)
        Points.setStyle('bold')
    if points >=250:
        Points.setFill('Blue')
        Points.setSize(36)
        Points.setStyle('bold italic')
    if points >= 500:
        Points.setFill('dark violet')
        Points.setSize(36)
        Points.setStyle('bold')

   
        
        
            
                

        

            
    
        
    
                
             



            

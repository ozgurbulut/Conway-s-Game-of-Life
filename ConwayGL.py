import turtle
import random
screen=turtle.Screen()
turtle.setup(1000,1000)
turtle.hideturtle()
turtle.speed(0)

hucreturtle = turtle.Turtle()
hucreturtle.up()
hucreturtle.hideturtle()
hucreturtle.speed(0)
hucreturtle.color('blue')

n = 15 # Orneklere bakilarak 15x15 kare secildi.
def cizgi(yatay_b,dikey_b,yatay_s,dikey_s):
    turtle.up()
    turtle.goto(yatay_b,dikey_b)
    turtle.down()
    turtle.goto(yatay_s,dikey_s)
    
def izgara_ciz(): 
    turtle.pencolor('black')
    turtle.pensize(1)
    x = -300
    for i in range(n+1):
        cizgi(x,-300,x,300)
        x += 600/n
    y = -300
    for i in range(n+1):
        cizgi(-300,y,300,y)
        y += 600/n

hucre = list()
def hucre_cagir():
    for i in range(n):
        hucrerow = [] # hucrelerin satirlari
        for j in range(n):
            if random.randint(0,7) == 0: 
                hucrerow.append(1) 
            else:
                hucrerow.append(0) 
        hucre.append(hucrerow) 
def kareyap(x,y,size): 
    hucreturtle.up()
    hucreturtle.goto(x,y)
    hucreturtle.down()
    hucreturtle.seth(0)
    hucreturtle.begin_fill()
    for i in range(4):
        hucreturtle.fd(size)
        hucreturtle.left(90)
    hucreturtle.end_fill()

def hucre_ciz(x,y):
    lx = 600/n*x - 300  
    ly = 600/n*y - 300
    kareyap(lx+1,ly+1,600/n-2)

def tamamini_ciz(): # Butun hucrelerin son hali
    global hucre
    for i in range(n):
        for j in range(n):
            if hucre[i][j] == 1: hucre_ciz(i,j)
izgara_ciz()
while(1):
	hucre_cagir()
	tamamini_ciz()
	screen.update()


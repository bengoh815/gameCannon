import turtle
from math import cos, sin

# screen
wn=turtle.Screen()
wn.setup(1200,600)


# cannon
cannon=turtle.Turtle()
cannon.penup()
cannon.speed(0)
cannon.setpos(-570,-270)
cannon.shapesize(2,2)

# cannonball
cannonball=turtle.Turtle()
cannonball.hideturtle()
cannonball.shape("circle")
cannonball.penup()
cannonball.speed(1)
cannonball.setpos(-570,-270)

# variables
time=0
cannonfiring=False
cannonpower=100
gravity=9.8
vx=abs(cannonpower*cos(cannon.heading()))
vy=abs(cannonpower*sin(cannon.heading()))


# functions
def turn_left():
    if cannon.heading() < 90:
        cannon.left(2)

def turn_right():
    if cannon.heading() > 0:
        cannon.right(2)

def cannonfire():
    cannonball.showturtle()
    cannonfiring=True

def cannonballupdate():
    global time, gravity, cannonfiring, vx, vy
    x = vx*time
    y = vy*time+(0.5*gravity*time*time)
    (cannonx, cannony)=cannonball.position()
    print(cannonball.position())
    # if cannony<=-280:
    cannonball.goto(x, y)
    if cannony>-280:
        cannonfiring=False
    time+=1


# listen
wn.listen()
wn.onkeypress(turn_left,"Up")
wn.onkeypress(turn_right,"Down")
wn.onkeypress(cannonfire,"space")



while True:
    wn.update()
    if cannonfiring==True:
        cannonballupdate()

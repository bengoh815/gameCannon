import turtle
from math import cos, sin, radians

# screen
wn=turtle.Screen()
wn.setup(1200,600)


# cannon
cannon=turtle.Turtle()
cannon.penup()
cannon.speed(0)
cannon.setpos(-570,-250)
cannon.shapesize(3,3)

# cannonball
cannonball=turtle.Turtle()
cannonball.hideturtle()
cannonball.shape("circle")
cannonball.penup()
cannonball.speed(0)
cannonball.goto(-570,-250)

# user select variables
angle=45
power=100
gravity=-9.81
print_cannonball_travel coordinates=False

# computer variables
time=0
cannon_trail=False
cannon_hit=False
cannon_fired=False


# function
def cannon_turn_left():
    if cannon.heading() < 90:
        cannon.left(1)

def cannon_turn_right():
    if cannon.heading() > 0:
        cannon.right(1)

def cannon_fire():
    global cannon_trail, cannon_fired
    cannon_fired=True
    cannonball.showturtle()
    if cannon_trail==True:
        cannonball.pendown()

def cannonball_update():
    global angle, time, power, gravity, cannon_hit, print_cannonball_travel
    x=(power*(cos(radians(angle)))*time)-570
    y=(power*(sin(radians(angle)))*time+(0.5*gravity*time*time))-250
    if print_cannonball_travel==True:
        print(x,y)
    if cannonball.ycor()>-251:
        cannonball.goto(x,y)
    else:
        cannonball.write("Cannonball has hit the ground")
        cannon_hit=True
    time+=0.5

# listen
wn.listen()
wn.onkeypress(cannon_turn_left,"Up")
wn.onkeypress(cannon_turn_right,"Down")
wn.onkeypress(cannon_fire,"space")


while True:
    wn.update()
    if (cannon_fired==True) and (cannon_hit==False):
        cannonball_update()
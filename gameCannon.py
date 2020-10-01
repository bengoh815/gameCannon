import turtle

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
cannonfiring=False
cannonpower=100


# functions
def turn_left():
    if cannon.heading() < 90:
        cannon.left(2)

def turn_right():
    if cannon.heading() > 0:
        cannon.right(2)

def cannonfire():
    global cannonfiring, cannonpower
    cannonball.showturtle()
    cannonfiring=True



# listen
wn.listen()
wn.onkeypress(turn_left,"Up")
wn.onkeypress(turn_right,"Down")
wn.onkeypress(cannonfire,"space")



while True:
    wn.update()
    if cannonfiring==True:
        # cannonball.goto()

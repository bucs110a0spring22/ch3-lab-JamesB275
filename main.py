import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
#SINGLE CALL FORWARD
michelangelo.forward(34)
leonardo.forward(81)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
leonardo.clear()
michelangelo.clear()

#TEN CALLS FORWARD
list_1=(1,2,3,4,5,6,7,8,9,10)
speed=(random.choice(list_1))
def turdspeed(turd,go):
   for i in range(11):
     michelangelo.forward(go)
     leonardo.forward(go)
turdspeed(michelangelo,speed)
turdspeed(leonardo,speed)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# Part B - complete part B here
leonardo.hideturtle()

michelangelo.down()
michelangelo.shape
michelangelo.color('purple')

def drawShape(turd,side):
  for i in range(side):
   turd.forward(25)
   turd.left(360/side)

drawShape(michelangelo,3)
michelangelo.clear()
drawShape(michelangelo,4)
michelangelo.clear()
drawShape(michelangelo,6)
michelangelo.clear()
drawShape(michelangelo,9)
michelangelo.clear()
drawShape(michelangelo,12)
michelangelo.clear()

window.exitonclick()
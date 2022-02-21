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
for i in range(10):
    for speed in [i,i,i,i,i,i,i,i,i,i]:
      print(michelangelo.forward(speed))
      print(leonardo.forward(speed))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# Part B - complete part B here
michelangelo.goto(-70,20)
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

michelangelo.up()
michelangelo.goto(-100,20)
window.exitonclick()
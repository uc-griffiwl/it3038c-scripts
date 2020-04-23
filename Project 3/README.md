# Introduction
I made a game similar to Space Invaders called Square Invaders! Your lone Triangle will need to destory as many squares as possible!
# Prerequisites
You will need to have VSCode and at least Python 3 installed in order to get this code to work. You can find downloads for these in the links below.
Python: https://www.python.org/downloads/
VSCode: https://code.visualstudio.com/download
# How to Run
After you have Python and VSCode installed. Open the Square Invaders.py file in VSCode and then right click on the code and click "Run Python file in Terminal" then you will be able to play the Square Invaders!
# Modules
You have to Import these modules in order to get the Square Invaders game to work.
``` javascript
import turtle
import os
import math
import random
```
# Set up the screen
This code will setup the screen that we will play Sqaure Invaders on.
``` javascript
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Square Invaders")
```
# Draw border
This code will setup the border around the gaming window.
``` javascript
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()	
```
# Set the score to 0
This code will set the scoreboard zero.
``` javascript
score = 0
```

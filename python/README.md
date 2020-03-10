# Introduction
I made the classic Snake Game in Python for Project 2 and this README.md will help explain my code.

# Modules
You have to Import these modules in order to get the Snake game to work.
``` javascript
import turtle
import time
import random
```
# Score
This sets up variables for the score board and setting the delay.
```javascript
delay = 0.1

score = 0
high_score = 0
```
# Gaming Window
This code will allow us to customize the window that the snake game will be played in.
``` javascript
wn = turtle.Screen()
wn.title("Wade's sneaky snake game")
wn.bgcolor("Magenta")
wn.setup(width=600, height=600)
wn.tracer(0) 
```
# Snake Head
This code allows us to customize the snakes head.
``` javascript
head = turtle.Turtle()
head.speed(0)
head.shape("triangle")
head.color("cyan")
head.penup()
head.goto(0,0)
head.direction = "stop"
```
# Snake Food
This code allows us to customize the snakes food.
``` javascript
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.penup()
head.goto(0,100)
```
# Segments
This line of code is a list command that will add a segment to the snake based on some code below in the main loop.
```javascript
segments = []
```
# Snake Body 
This code allows us to customize the snakes body and update the scoreboard when it adds a body part.
```javascript
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("orange")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score 0", align="center", font=("Chiller", 20, "normal"))
```
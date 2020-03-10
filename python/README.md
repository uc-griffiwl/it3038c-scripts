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
setting up variables for the score board and setting the delay.
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

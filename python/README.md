# Introduction
I made the classic Snake Game in Python for Project 2 and this README.md will help explain my code.
# Prerequisites
You will need to have VSCode and at least Python 3 installed in order to get this code to work. You can find downloads for these in the links below.
Python: https://www.python.org/downloads/
VSCode: https://code.visualstudio.com/download
# How to Run
After you have Python and VSCode installed. Open the snake.py file in VSCode and then right click on the code and click "Run Python file in Terminal" then you will be able to play the classic Snake game!
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
# Snake Movement
This def and if statements allow the snake to move around the game grid up, down, left, and right.
```javascript
def go_up():
    if head.direction != "down":
        head.direction ="up"

def go_down():
    if head.direction != "up":
        head.direction ="down"

def go_left():
    if head.direction != "right":
        head.direction ="left"

def go_right():
    if head.direction !="left":
        head.direction ="right"

def move():
    if head.direction =="up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction =="down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction =="left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction =="right":
        x = head.xcor()
        head.setx(x + 20)
```
# Keyboard Bindings
This codes allows w, s, a, d keys to be bind to the game window in order to move the snake.
```javascript
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
```
# Main Game Loop
This code says that while the game window is open, update the game.
```javascript
while True:
    wn.update()
   ```
# Setting collisions with the Border
This codes sets the boundries to the gaming window so the game will end if you hit the border.
```javascript
if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction ="stop"
```
# Hides segments
This hides segments of the snake before they are earned for eating the food.
```javascript
for segment in segments:
        segment.goto(1000,1000)
```
# Clear segment list
This code clears segments added to the snake body.
```javascript
segments.clear()
```
# Reset Score and Delay
This code resets the score and delay. 
```javascript
score = 0
delay = 0.1
```
# Snake eating food
This code allows the snake head to collide with the food.
```javascript
if head.distance(food) < 20:
```
# Food Regenerating
This code moves the food at random around the gaming window.
```javascript
x = random.randint(-290,290)
        y= random.randint(-290,290)
        food.goto(x,y)
```
# Adding to the snake body
This code allows us to customize the snake body after it eats the food.
```javascript
new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)
```
# Update Score
This code will shorten the delay and increase the score and reflect the change on the scoreboard.
```javascript
delay -= 0.001

score +=10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score {}".format(score, high_score), align ="center", font=("Chiller", 20, "normal"))
```
# Moving the Snakes body
This codes for loop explains how the snakes body moves in reverse order.
```javascript
for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
```
# Snake body placement
This if statment explains how the snake body will start to grow from the snakes head and expand the body upon that.
```javascript
if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
```
# Move
This allows the Snake to move.
```javascript
move()
```
# Snake Head hitting the body
This code explains how the game checks to see if the snake head collides with the snake body.
```javascript
for segment in segments:
        if segment.distance(head) <20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
```
# Post move code
This code explains how we hide segments, clear segments, reset score, reset delay, and update the score.
```javascript
for segment in segments:
                segment.goto(1000, 1000)
                
            segments.clear()

            score = 0

            delay = 0.1

            pen.clear()
            pen.write("Score {} High Score {}".format(score, high_score), align="center", font=("Chiller", 20, "normal"))
```
# Ending of Code
This code ends the delay and mainloop.
```javascript
    time.sleep(delay)

wn.mainloop()
```

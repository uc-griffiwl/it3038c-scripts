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
# Draw the scoreboard
This code will setup the scoreboard and keep track of the score.
``` javascript
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()
```
# Create the player turtle
This code creates the lone triangle character you have to make survive the squares!
``` javascript
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15
```
# Choose A Number of Enemies
This code will create the amount of enemies your triangle will be facing.
``` javascript
number_of_enemies = 5
```
# Create an empty list of enemies
This code will create a list of emenmies.
``` javascript
enemies = []
```
# Add enemies to the list
This code will add enemies to the list and allow you to customize your enemies.
``` javascript
for i in range(number_of_enemies):
	#Create the enemy
	enemies.append(turtle.Turtle())

for enemy in enemies:
	enemy.color("red")
	enemy.shape("square")
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200, 200)
	y = random.randint(100, 250)
	enemy.setposition(x, y)

enemyspeed = 2
```
# Create the player's bullet
This code allows us to create and customize the triangle's bullets.
``` javascript
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("circle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20
```
# Define bullet state
This code allows the bullet to be shot at the squares.
``` javascript
bulletstate = "ready"
```
# Move the player left and right
This code allows you to move your triangle left and right of the screen.
``` javascript
def move_left():
	x = player.xcor()
	x -= playerspeed
	if x < -280:
		x = - 280
	player.setx(x)
	
def move_right():
	x = player.xcor()
	x += playerspeed
	if x > 280:
		x = 280
	player.setx(x)
```
# Declare the bulletstate global
This code will allow your bullet to shoot from anywhere in the border.
``` javascript
def fire_bullet():
	global bulletstate
	if bulletstate == "ready":
		bulletstate = "fire"
```
# Move the bullet to the just above the player
This code will place make the bullet shoot out the end point of the triangle.
``` javascript
x = player.xcor()
y = player.ycor() + 10
bullet.setposition(x, y)
bullet.showturtle()
def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 15:
		return True
	else:
		return False
```
# Create keyboard bindings
This code bind the game controls to buttons on your keyboard.
``` javascript
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")
```
# Main Game Loop
This code is what runs the game, moves the enemies, checks for colliosn with bullet and enemy, resets the bullets, updates the scoreboard, moves the bullet, checks to see if the bullet is out the border at the top, and then lastly will reset the game. The main game loop has a lot going on and combines all these elements.
``` javascript
while True:
	
	for enemy in enemies:
		#Move the enemy
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)

		#Move the enemy back and down
		if enemy.xcor() > 280:
			#Move all enemies down
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			#Change enemy direction
			enemyspeed *= -1
		
		if enemy.xcor() < -280:
			#Move all enemies down
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			#Change enemy direction
			enemyspeed *= -1
			
		#Check for a collision between the bullet and the enemy
		if isCollision(bullet, enemy):
			#Reset the bullet
			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0, -400)
			#Reset the enemy
			x = random.randint(-200, 200)
			y = random.randint(100, 250)
			enemy.setposition(x, y)
			#Update the score
			score += 10
			scorestring = "Score: %s" %score
			score_pen.clear()
			score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
		
		if isCollision(player, enemy):
			player.hideturtle()
			enemy.hideturtle()
			print ("Game Over")
			break

		
	#Move the bullet
	if bulletstate == "fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)
	
	#Check to see if the bullet has gone to the top
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate = "ready"
		
delay = raw_input("Press enter to finsh.")
```

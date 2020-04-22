import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Gandolfs Gold")
wn.setup (700,700)

#Create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
#Create player
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
#Move player
    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 24)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 24)

    def go_left(self):
        self.goto(self.xcor() - 24, self.ycor())

    def go_right(self):
        self.goto(self.xcor() + 24, self.ycor())

#Create levels list
levels = [""]

#Define first level
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXP             XXXXXXXX",
"XXX      XXXXXX    XXXXXX",
"XXXXXX   XXXXXXX   XXXXXX",
"XXXXX    XXXXXXX   XXXXXX",
"X  XX    XXXXXXX   XXXXXX",
"X  XX    XXXXXXXXXXXXXXXX",
"X  XX       XXXXXXXXXXXXX",
"X      XXX   XXXXXXXXXXXX",
"XXXXX   XX   XXXXX    XXX",
"XXXXX   XX   XXXXX    XXX",
"XXXXX   XX   XXXXXXX   XX",
"XXXXXXXXXX     XXXXX    X",
"XXXXXXXXXX     XXXXXX   X",
"XXXX         XXXXXXXX   X",
"XXXXXXX                 X",
"XXXXXXXXXXXXXXXXX       X",
"XXXXXXXXXXXXXXXXX       X",
"X    XXXXXXXXXXXX   XXXXX",
"X    XXXXXXXX       XXXXX",
"X      XXXXXXXXXX    XXXX",
"XXXX     XXXXXXXXX    XXX",
"X  X    XXXXXXX      XXXX",
"X  XX   XXXXXXXXX    XXXX",
"X                    XXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]

#Add maze to maze list
levels.append(level_1)

#Create level setup function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #get the character at each x,y coordinate
            character = level[y][x]
            #Calculate the screen x, y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            #Check if it is an X (X being a wall)
            if character =="X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
            #Check if it is a P (Represting player)
            if character == "P":
                player.goto(screen_x, screen_y)

#Create class instances
pen = Pen()
player = Player ()
#Set up the level
setup_maze(levels[1])

#Keyboard binding
turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")

#turn off screen updates
wn.tracer(0)

#main game loop
while True:
    pass
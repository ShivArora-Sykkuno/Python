import turtle as t
import random

""" Billu The Turtle can draw what you want him to draw 
	using your keyboard as space to draw, (up, down , left, right) to change directions,
	n to choose a color, r to reset it a to increase the pen size, s to decrease the pensize,
	q for not drawing and just moving and w to go back on drawing
"""
def jumping():
	billu.penup()

def clear_jump():
	billu.pendown()

def clear():
	billu.home()
	billu.penup()
	billu.clear()
	billu.pendown()

def choose_color():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	Color = (r, g, b)
	billu.color(Color)

def add_thickness():
	global a
	a = a + 1
	billu.pensize(a)

def sub_thickness():
	global a
	a -= 1
	billu.pensize(a)

def move_forward():
	billu.forward(10)


def turn_up():
	billu.setheading(90)


def turn_down():
	billu.setheading(270)


def turn_left():
	billu.right(10)


def turn_right():
	billu.left(10)


screen = t.Screen()
billu = t.Turtle()
billu.shape("turtle")
a = 1
t.colormode(255)
screen.listen()

# Function My turtle can Do
screen.onkey(key = "space", fun = move_forward)
screen.onkey(key = "Up", fun = turn_up)
screen.onkey(key = "Down", fun = turn_down)
screen.onkey(key = "Right", fun = turn_left)
screen.onkey(key = "Left", fun = turn_right)
screen.onkey(key = "n", fun = choose_color)
screen.onkey(key = "a", fun = add_thickness)
screen.onkey(key = "s", fun = sub_thickness)
screen.onkey(key = "r", fun = clear)
screen.onkey(key = "q", fun = jumping)
screen.onkey(key = "w", fun = clear_jump)



screen.exitonclick()

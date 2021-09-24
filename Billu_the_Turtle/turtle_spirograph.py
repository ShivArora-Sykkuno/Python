import turtle as t
import random

def choose_color():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	color = (r, g, b)
	return color

def spirograph():
	for i in range(72):
		billu.color(choose_color())
		billu.circle(200)
		billu.right(5)


screen = t.Screen()
billu = t.Turtle()
billu.shape("turtle")
t.colormode(255)
billu.pensize(2)
spirograph()




screen.exitonclick()
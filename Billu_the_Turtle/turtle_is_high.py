import turtle as t
import random
def drawing(sides, color):
	angel = 360/sides
	billu.color(color)
	for i in range(sides):
		billu.forward(100)
		billu.right(angel)

def choose_color():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	color = (r, g, b)
	return color

def choose_direction(direction):
	dir = random.choice(direction)
	return dir

screen = t.Screen()
billu = t.Turtle()
billu.shape("turtle")
t.colormode(255)
colors = ["red", "blue", "green", "orange", "cyan", "chocolate", "DarkOrchid", "violet red"]
directions = [90, 180, 270, 360]

flag = 0
while(flag != 1):
	billu.speed("fast")
	billu.pensize(10)
	billu.color(choose_color())
	billu.right(choose_direction(directions))
	billu.forward(30)



screen.exitonclick()
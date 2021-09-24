import turtle as t
import random
import colorgram

def color_extraction(file_name):
	colors = colorgram.extract(file_name, 10)
	rgb_colors = []
	for color in colors:
		r = color.rgb.r
		g = color.rgb.g
		b = color.rgb.b
		new_color = (r, g, b)
		rgb_colors.append(new_color)
	return rgb_colors


def choose_color(rgb_colors):
		return random.choice(rgb_colors)


def painting():
	billu.hideturtle()
	for j in range(10):
		for i in range(10):
			billu.color(choose_color(rgb_colors))
			billu.forward(0)
			billu.penup()
			billu.forward(50)
			billu.pendown()
		billu.setheading(90)
		billu.penup()
		billu.forward(50)
		billu.setheading(180)
		billu.forward(500)
		billu.pendown()
		billu.setheading(0)



screen = t.Screen()
billu = t.Turtle()
billu.shape("turtle")
t.colormode(255)
billu.speed("slow")
billu.pensize(20)


rgb_colors = color_extraction("color_pallet.jpg")
painting()


screen.exitonclick()
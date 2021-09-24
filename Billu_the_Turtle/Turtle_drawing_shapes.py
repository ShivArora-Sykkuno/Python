from turtle import Turtle, Screen

def drawing(sides, color):
	angel = 360/sides
	billu.color(color)
	for i in range(sides):
		billu.forward(100)
		billu.right(angel)


screen = Screen()
billu = Turtle()
billu.shape("turtle")
colors = ["red", "blue", "green", "orange", "cyan", "chocolate", "DarkOrchid", "violet red"]
for i in range(3, 11):
	billu.shapesize(2)
	billu.pensize(3)
	color = colors[i-3]
	drawing(i, color)
# Square()
# length = int(input("Enter the length of the dashed line "))
# dashed_line(length)



screen.exitonclick()
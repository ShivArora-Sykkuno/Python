import turtle as t
import random

"""Race 5 Turtles and bet on your favourite turtle and 
	we will see Who will Win the Race
	"""

screen = t.Screen()
screen.setup(width = 530, height = 400)
is_race_on = False
user_bet = screen.textinput(title = "Make You Bet", prompt = "Which One of the turtle will win the race")
colors = ["red", "yellow", "green", "orange", "blue", "purple"]
y_coordinates = [0, 35, 70, 105, -35, -70]
all_turtles = []



for i in range(6):
	new_turtle = t.Turtle(shape = "turtle")
	new_turtle.speed("slowest")
	new_turtle.color(colors[i])
	new_turtle.penup()
	new_turtle.goto(x= -250, y= y_coordinates[i])
	all_turtles.append(new_turtle)




if user_bet:
	is_race_on = True



while is_race_on:
	for turtle in all_turtles:
		if turtle.xcor() > 240:
			is_race_on = False
			winning_color = turtle.pencolor()
			if winning_color == user_bet:
				print(f"You have Won! The {winning_color} turtle is the Winner")
			else:
				print(f"You have Lost! The {winning_color} turtle is the Winner")
		speed = random.randint(1, 5)
		turtle.forward(speed)

screen.exitonclick()

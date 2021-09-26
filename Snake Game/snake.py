from turtle import Turtle
import turtle as t
import random

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0), (-80, 0)]
MOVE_DISTANCE = 15


class Snake:

	def __init__(self):
		self.colorp = (255, 255, 255)
		self.all_snake_body = []
		self.create_snake()
		self.head = self.all_snake_body[0]
		self.snake_pos = 0


	def create_snake(self):
		for i in STARTING_POSITIONS:
			self.add_segment(i)

	def add_segment(self, position):
		self.snake = Turtle("square")
		t.colormode(255)
		self.snake.color(self.colorp)
		self.snake.speed("slow")
		self.snake.penup()
		self.snake.goto(position)
		self.all_snake_body.append(self.snake)

	def change_color(self):
		r = random.randint(70, 255)
		g = random.randint(70, 255)
		b = random.randint(70, 255)
		self.colorp = (r, g, b)
		for body in self.all_snake_body:
			body.color(self.colorp)

	def extend_snake(self):
		self.add_segment(self.all_snake_body[-1].position())

	def move_snake(self):
		for snake_num in range(len(self.all_snake_body) - 1, 0, -1):
			new_x = self.all_snake_body[snake_num - 1].xcor()
			new_y = self.all_snake_body[snake_num - 1].ycor()
			self.all_snake_body[snake_num].goto(new_x, new_y)

		self.all_snake_body[0].forward(MOVE_DISTANCE)

	def snake_up(self):
		if self.snake_pos == 3:
			pass
		else:
			self.head.setheading(90)
			self.snake_pos = 1

	def snake_down(self):
		if self.snake_pos == 1:
			pass
		else:
			self.head.setheading(270)
			self.snake_pos = 3

	def snake_left(self):
		if self.snake_pos == 0:
			pass
		else:
			self.head.setheading(180)
			self.snake_pos = 2

	def snake_right(self):
		if self.snake_pos == 2:
			pass
		else:
			self.head.setheading(360)
			self.snake_pos = 0

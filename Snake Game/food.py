import random
from turtle import Turtle


class Food(Turtle):

	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.penup()
		self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
		self.color("blue")
		self.speed("fastest")
		self.deploy_food()



	def deploy_food(self):
		self.x_food = random.randint(-270, 270)
		self.y_food = random.randint(-270, 270)
		self.goto(self.x_food, self.y_food)

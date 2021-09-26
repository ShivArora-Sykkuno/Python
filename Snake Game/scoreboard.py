from turtle import Turtle
FONT = "Courier"
FONT_SIZE = 16
FONT_TYPE = "bold"
ALIGNMENT = "center"

class ScoreBoard(Turtle):

	def __init__(self):
		super().__init__()
		self.score = 0
		self.color("White")
		self.speed("fastest")
		self.hideturtle()
		self.penup()
		self.goto(0, 270)
		self.update_scoreboard()


	def increase_score(self):
		self.score += 1
		self.clear()
		self.update_scoreboard()

	def update_scoreboard(self):
		self.write(arg = f"Snake Score: {self.score}",align = ALIGNMENT,  font = (FONT, FONT_SIZE, FONT_TYPE))


	def game_over(self):
		self.goto(0, 0)
		self.write(arg = "GAME OVER", align = ALIGNMENT, font = (FONT, FONT_SIZE, FONT_TYPE))
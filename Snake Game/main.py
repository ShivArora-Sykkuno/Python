import turtle as t
import time
from snake import *
from food import *
from scoreboard import *


screen = t.Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.onkey(key = "Up", fun = snake.snake_up)
screen.onkey(key = "Down", fun = snake.snake_down)
screen.onkey(key = "Left", fun = snake.snake_left)
screen.onkey(key = "Right", fun = snake.snake_right)
screen.onkey(key = "q", fun = snake.change_color)

start_game = True
while start_game:
	screen.update()
	time.sleep(0.1)
	snake.move_snake()

	# Detect the Collision with the snake
	if(snake.head.distance(food) < 15):
		food.deploy_food()
		snake.extend_snake()
		score_board.increase_score()

	# Detect Collision With the Wall
	if(snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290):
		start_game = False
		score_board.game_over()

	# Detect the collision with the tail
	for body in snake.all_snake_body[1:]:

		if (snake.head.distance(body) < 10):
			start_game = False
			score_board.game_over()




screen.exitonclick()

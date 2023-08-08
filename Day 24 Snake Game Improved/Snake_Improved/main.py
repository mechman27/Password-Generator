import turtle as t
import random as r
import time 
from snake import Snake
from food import Food
from score import Scoreboard

s = t.Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.05)
    snake.move()
    #detect collision with food
    if snake.head.distance(food) < 15:
        food.reset()
        snake.extend()
        score.increase_score()
    #detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score.reset_score()
        snake.reset()
    #detect collision with itself
    for segment in snake.snake_body[1:len(snake.snake_body) - 1]:
        if snake.head.distance(segment) < 5:
            score.reset_score()
            snake.reset()
            

s.exitonclick()
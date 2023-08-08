import turtle as t
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

s = t.Screen()
s.bgcolor("black")
s.setup(width=800, height=600)
s.title("Pong")
s.tracer(0)


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Scoreboard()

s.listen()
s.onkey(r_paddle.go_up, "Up")
s.onkey(r_paddle.go_down, "Down")

game_is_on = True

while game_is_on:
    s.update()
    #time.sleep(0.05)
    ball.move()
    if r_paddle.ycor() < 280:
        r_paddle.go_up
    #detect collision with the wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    if ball.xcor() > 340 and ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    if ball.xcor() < -380:
        ball.reset()
        score.r_point()
    if ball.xcor() > 380:
        ball.reset()
        score.l_point()




s.exitonclick()
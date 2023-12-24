from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

paddle1 = Paddle(350, 0)
paddle2 = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")

screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

flag=True

while flag:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

#     detect ball collision with WALL

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # ball collision with paddle
    if ball.distance(paddle1)<50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # right miss
    if ball.xcor() > 380:
        ball.pos_reset()
        scoreboard.l_point()

#     left miss

    if ball.xcor() < -380:
        ball.pos_reset()
        scoreboard.r_point()


screen.exitonclick()
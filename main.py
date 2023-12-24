from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

paddle1 = Paddle(350, 0)
paddle2 = Paddle(-350, 0)
ball = Ball()

screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")

screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

flag=True

while flag:
    screen.update()
    ball.move()
    time.sleep(0.1)

screen.exitonclick()
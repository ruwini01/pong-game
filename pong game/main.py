from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


def restart():
    is_game_on = True
    while is_game_on:

        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Detect collision with wall and bounce
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.y_bounce()

        # Detect Collision with Paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.x_bounce()

        if ball.xcor() > 400:
            scoreboard.l_increase_score()
            ball.reset_position()

        if ball.xcor() < -400:
            scoreboard.r_increase_score()
            ball.reset_position()


restart()

screen.exitonclick()

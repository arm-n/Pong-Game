import turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


POSITION = [(350,0),(-350,0),(0,0)]
SPEED = 1

tom = turtle.Turtle()
screen = turtle.Screen()
screen.screensize(canvwidth=800,canvheight=600,bg='black')

screen.title("Pong")
r_paddle = Paddle(POSITION[0])
l_paddle = Paddle(POSITION[1])
ball = Ball(POSITION[2])
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")

screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ball.ycor() > 290 or ball.ball.ycor() < -290:
        ball.bounce_y()

    # Ball Collision with Left/Right Walls (Out of bounds)
    if (ball.ball.xcor() > 330 and ball.ball.distance(r_paddle.paddle) < 50 or ball.ball.xcor() < -330 and
            ball.ball.distance(l_paddle.paddle) < 50):
        ball.bounce_x()



        #detects if r paddle misses
    elif ball.ball.xcor() > 350 :
        ball.reset_position()
        scoreboard.l_point()

    # detects if r paddle misses
    elif ball.ball.xcor() < -350:
        ball.reset_position()
        scoreboard.r_point()









screen.exitonclick()


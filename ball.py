import turtle
POSITION = [(0,0)]

class Ball:

    def __init__(self,position):
        self.ball = turtle.Turtle("circle")
        self.ball.penup()
        self.ball.color('beige')
        self.ball.goto(position)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    def move(self):
        new_x = self.ball.xcor() + self.x_move
        new_y = self.ball.ycor() + self.y_move
        self.ball.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1  # Reverse vertical direction

    def bounce_x(self):
        self.x_move *= -1  # Reverse horizontal direction
        self.move_speed *= 0.9

    def reset_position(self):
        self.ball.speed("fastest")
        self.ball.goto(0, 0)
        self.move_speed = 0.05
        self.bounce_x()

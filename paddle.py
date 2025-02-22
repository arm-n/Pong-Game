import turtle

UP = 90
DOWN = 270
POSITION = [(350,0),(-350,0)]

class Paddle:

    def __init__(self,position):
        self.paddle = turtle.Turtle('square')
        self.paddle.speed('fastest')
        self.paddle.penup()
        self.paddle.goto(position)  
        self.paddle.color('beige')
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)  # Paddle size

    def up(self):
        if self.paddle.ycor() < 250:
            y = self.paddle.ycor()  # Get current Y coordinate
            self.paddle.sety(y + 20)  # Move paddle up by 20 units

    def down(self):
        if self.paddle.ycor() > -250:
            y = self.paddle.ycor()  # Get current Y coordinate
            self.paddle.sety(y - 20)  # Move paddle down by 20 units

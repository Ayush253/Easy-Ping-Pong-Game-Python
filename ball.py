from turtle import Turtle
import random

COLORS = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "gray", "white"]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def create_game_border(self):
        game_border = Turtle()
        game_border.penup()
        game_border.setposition(-380, -320)
        game_border.pendown()
        game_border.pensize(3)
        game_border.color("white")
        for i in range(2):
            game_border.forward(760)
            game_border.left(90)
            game_border.forward(630)
            game_border.left(90)
        game_border.hideturtle()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.color(random.choice(COLORS))
        self.bounce_x()
from turtle import Turtle, Screen
import time

def snake():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake in Python")
    screen.listen()
    screen.tracer(0)

    game_is_on = True
    snake_bits = []
    positions = [(0, 0), (-20, 0), (-40, 0)]
    for bit in range(0,3):
        new_snake_bit = Turtle(shape="square")
        new_snake_bit.penup()
        new_snake_bit.color("white")
        new_snake_bit.speed(1)
        new_snake_bit.goto(positions[bit])
        snake_bits.append(new_snake_bit)

    while game_is_on:
        screen.update()
        time.sleep(.1)
        for bit_num in range(2, 0, -1):
            new_x = snake_bits[bit_num -1].xcor()
            new_y = snake_bits[bit_num - 1].ycor()
            snake_bits[bit_num].goto(new_x, new_y)
        screen.exitonclick()

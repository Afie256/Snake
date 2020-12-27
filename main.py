# Day 2
# TODO Detect collision with food
# TODO Create a scoreboard
# TODO Detect wall collision
# TODO Detect collision with tail


from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake in Python")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_is_on = True
while game_is_on:
    screen.tracer(0)
    screen.update()
    time.sleep(0.09)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collation with tail
    # If head collides with any segment in the tail:
    # Trigger game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()

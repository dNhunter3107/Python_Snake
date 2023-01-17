from turtle import Screen
from snakes import Snake
from food import Food
from score import Scoreboard
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("blue")
screen.title("My Snakes Game")

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -300:
        score.reset_progress()
        snake.reset_snakes()

    if snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -300:
        score.reset_progress()
        snake.reset_snakes()

    for segments in snake.segments:
        if segments == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segments) < 10:
            score.reset_progress()
            snake.reset_snakes()

screen.exitonclick()

from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
        #score.game_over()
        #is_on = False

    for seg in snake.segments:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            score.reset()
            snake.reset()
            #is_on = False
            #score.game_over()
screen.exitonclick()

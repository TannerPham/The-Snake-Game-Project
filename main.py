from snake import Snake
from turtle import Screen
from scoreboard import Scoreboard
from border import Border
import time
from food import Food
# set up the screen
screen = Screen()
screen.setup(height=640,width=800)
screen.bgcolor("black")
screen.title("The greatest game of my childhood")
screen.tracer(0)
border = Border()
border.draw_border()

# Step 1: Create the snake body

snake = Snake()
food = Food()
scoreboard = Scoreboard()

snake.create_snake()

screen.listen()
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_down,"Down")
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_right,"Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    # detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.gameover()
    # delect collision with tail

    for segment in snake.segments[1:]: #slice the segments list from 1 to end, omit the 0 index
        if snake.head.distance(segment)< 10:
            game_is_on = False
            scoreboard.gameover()



    





screen.exitonclick()

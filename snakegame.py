
from turtle import Screen
from scoreboard import*
from snake import Snake
import time
from FOOD import Food
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()

snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey( snake.right,"Right")

screen.update()
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    #collision detection
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        print("Game Over")
        game_is_on=False
        scoreboard.game_over()

    #detect collision with tail
    for segment in snake.new:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on=False
            scoreboard.game_over()



screen.exitonclick()






















screen.exitonclick()
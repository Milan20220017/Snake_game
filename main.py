import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
snake=Snake()
food=Food()
rezultat=ScoreBoard()
screen.title("My snake game")
screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

 # Detect collision between snake and food
    for segments in snake.segments[1:]:
        if snake.head.distance(segments)<15:
            rezultat.reset()
            snake.reset()
    if snake.head.distance(food)<15:
        snake.extend()
        food.refresh()
        rezultat.povecaj()
# detected collision with wall.
    if snake.head.xcor()>290 or snake.head.ycor()>290 or snake.head.xcor()<-290 or snake.head.ycor()<-290:
        rezultat.reset()
        snake.reset()


screen.exitonclick()
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("ヘビゲーム")
screen.tracer(0)  # turn turtle animation off

snake = Snake()
food = Food()
scoreboard = Scoreboard()

input_error = False

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_active = True

while game_is_active:
    screen.update()  # perform a TurtleScreen update (used when tracer is turned off)
    snake.set_difficulty()
    snake.snake_movement()

    # food collision detection
    if snake.head.distance(food) < 10:
        for block in snake.blocks:
            if food.distance(block) < 10:  # avoid the overlapping of food and snake body
                food.refresh()
        snake.extend_body()
        scoreboard.increase_score()

    # wall collision detection
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_active = False
        scoreboard.game_over()

    # tail collision detection
    for block in snake.blocks[1:]:
        if snake.head.distance(block) < 10:
            game_is_active = False
            scoreboard.game_over()

screen.exitonclick()

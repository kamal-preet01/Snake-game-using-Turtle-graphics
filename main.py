# snake game using turtle
from turtle import Turtle, Screen
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Kamal ki sasti snake game")
screen.tracer(0)

starting_pos = [(0, 0), (-20, 0), (-40, 0)]
segment = []

for pos in starting_pos:
    kp_turtle = Turtle(shape="square")
    kp_turtle.penup()
    kp_turtle.color("white")
    kp_turtle.goto(pos)
    segment.append(kp_turtle)

up=90
down=270
right=0
left=180


def move_up():
    if segment[0].heading()!=down:
        segment[0].setheading(up)
def move_down():
    if segment[0].heading()!=up:
        segment[0].setheading(down)
def move_left():
    if segment[0].heading()!=right:
        segment[0].setheading(left)
def move_right():
    if segment[0].heading()!=left:
        segment[0].setheading(right)

screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")




food_turtle=Turtle()
food_turtle.shape("circle")
food_turtle.penup()
food_turtle.shapesize(stretch_len=0.5,stretch_wid=0.5)
food_turtle.color("blue")
food_turtle.speed("fastest")
random_x=random.randint(-280,280)
random_y=random.randint(-280,280)
food_turtle.goto(random_x,random_y)

score_turtle=Turtle()
score=0
score_turtle.color("red")
score_turtle.penup()
score_turtle.goto(0,270)
score_turtle.write(f"Score : {score}",align="center",font=("Arial",24,"normal"))
score_turtle.hideturtle()




game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    if segment[0].distance(food_turtle) < 15:
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        food_turtle.goto(random_x, random_y)
        score=score+1
        score_turtle.clear()
        score_turtle.write(f"Score : {score}", align="center", font=("Arial", 24, "normal"))



    for seg_num in range(2, 0, -1):
        new_x = segment[seg_num - 1].xcor()
        new_y = segment[seg_num - 1].ycor()
        segment[seg_num].goto(new_x, new_y)
    segment[0].forward(20)

    if(segment[0].xcor()>280 or segment[0].xcor()<-280 or segment[0].ycor()>280 or segment[0].ycor()<-280):
        game_is_on = False
        game_over = Turtle()
        game_over.color("red")
        game_over.write("GAME OVER ! looser!!", align="center", font=("Arial", 24, "normal"))
        game_over.hideturtle()





screen.exitonclick()

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=1350, height=900)
screen.bgpic('tracks.png')

ALIGN = "right"
FONT = ("Cambria", 24, "bold")

y_positions = [310, 160, 10, -140, -290]
colors = ['purple', 'red', 'blue', 'dark green', 'black']
all_turtles = []
user_bet = screen.textinput('Enter your bet', prompt='Which turtle (colour):')

for index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.shapesize(2)
    new_turtle.speed('fastest')
    new_turtle.penup()
    new_turtle.goto(x=-645, y=y_positions[index])
    new_turtle.color(colors[index])
    all_turtles.append(new_turtle)

is_on = True

while is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 610:
            is_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                turtle.write(f'Congratulations! {winner} turtle is the winner', font=FONT, align=ALIGN)
            else:
                turtle.write(f'Sorry, you lost! {winner} turtle is the winner', font=FONT, align=ALIGN)
        random_pace = random.randint(20, 50)
        turtle.forward(random_pace)

screen.exitonclick()

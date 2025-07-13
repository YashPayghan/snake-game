from turtle import *
value=[(0,0),(-20,0),(-40,0)]
distance=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.new=[]
        self.create_snake()
        self.head=self.new[0]

    def create_snake(self):
        for index in value:
            self.add_tail(index)

    def  add_tail(self,index):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(index)
        self.new.append(new_turtle)

    def extend(self):
        self.add_tail(self.new[-1].position())


    def move(self):
        for seg_num in range(len(self.new) - 1, 0, -1):
            new_x = self.new[seg_num - 1].xcor()
            new_y = self.new[seg_num - 1].ycor()
            self.new[seg_num].goto(new_x, new_y)
        self.head.forward(distance)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
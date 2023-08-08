import turtle as t
import time
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
START_POSITION = [(0, 0), (-20, 0), (-40,0)]
class Snake:
    def __init__(self):
        self.snake_body = []
        self.setup()
        self.head = self.snake_body[0]
        

    def setup(self):
        for position in START_POSITION:
            self.add_segment(position)
            

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading()!= LEFT:    
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)


    def move(self):
        for piece in range(len(self.snake_body) - 1, 0 , -1):
            new_x = self.snake_body[piece-1].xcor()
            new_y = self.snake_body[piece-1].ycor()
            self.snake_body[piece].goto(new_x, new_y)
        self.head.forward(10)
                
    def add_segment(self, position):
        snake_head = t.Turtle(shape="square")
        snake_head.color("white")
        snake_head.penup()
        snake_head.goto(position)
        self.snake_body.append(snake_head)
    
    def reset(self):
        for segment in self.snake_body:
            segment.goto(1000, 1000)
        self.snake_body.clear()
        self.setup()
        self.head = self.snake_body[0]

    def extend(self):
        self.add_segment(self.snake_body[-1].position())
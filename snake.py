from turtle import Turtle, Screen
import time
from tkinter import messagebox

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

# orientation of the snake in angles
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.blocks = []  # body blocks of the snake
        self.create_snake_body()
        self.head = self.blocks[0]
        self.difficulty_choice = Screen().textinput(title="ヘビゲーム",
                                                    prompt="Control the snake by using the arrow keys.\n\n"
                                                           "Select a difficulty (easy, normal, hard):\n")

    def create_snake_body(self):
        for position in STARTING_POSITIONS:
            self.add_blocks(position)

    def snake_movement(self):
        for block_index in range(len(self.blocks) - 1, 0, -1):
            new_x = self.blocks[block_index - 1].xcor()  # return the snake’s x coordinate
            new_y = self.blocks[block_index - 1].ycor()  # return the snake’s y coordinate
            self.blocks[block_index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def set_difficulty(self):
        if self.difficulty_choice == "normal":
            time.sleep(0.1)  # suspend execution of the calling thread for 0.1 second (delay refresh of the animation)
        elif self.difficulty_choice == "hard":
            time.sleep(0.05)
        elif self.difficulty_choice == "easy":
            time.sleep(0.2)
        else:
            Screen().bye()
            messagebox.showerror("Error", "Invalid Input: restart the game and provide a valid input.")

    def up(self):
        if self.head.heading() != DOWN:  # get and validate snake_head's heading angle
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

    def add_blocks(self, position):
        new_block = Turtle("square")
        new_block.color("white")
        new_block.penup()
        new_block.goto(position)
        self.blocks.append(new_block)

    def extend_body(self):
        self.add_blocks(self.blocks[-1].position())  # get the position of the last block and add one block behind it

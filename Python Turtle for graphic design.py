# This is for a YouTube tutorial https://youtu.be/ff1h7bQEg68

import turtle
import random

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object for background pattern
pattern = turtle.Turtle()
pattern.penup()

# Define the background pattern parameters
pattern_size = 40
pattern_colors = ["pale green", "light yellow"]

# Draw the background pattern
for x in range(-screen.window_width() // 2, screen.window_width() // 2, pattern_size):
    for y in range(-screen.window_height() // 2, screen.window_height() // 2, pattern_size):
        pattern.goto(x, y)
        pattern.color(random.choice(pattern_colors))
        pattern.begin_fill()
        for _ in range(4):
            pattern.forward(pattern_size)
            pattern.right(90)
        pattern.end_fill()

# Hide the pattern turtle
pattern.hideturtle()

# Update the screen
screen.update()

# Exit on click
screen.exitonclick()

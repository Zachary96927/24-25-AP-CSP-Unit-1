#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

index = 0

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.color(turtle_colors.pop())
  index += 1
  t.penup()
  my_turtles.append(t)


#Where the turtle starts
startx = 0
starty = 0

#How much the shape moves

for t in my_turtles:
  t.goto(startx, starty)
  t.right(45)
  t.forward(50)
  turtle.penup()
#where the next shape begins after each shape
  startx = startx + 50
  starty = starty + 50
  turtle.goto(startx, starty)


wn = trtl.Screen()
wn.mainloop()
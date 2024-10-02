#   a116_ladybug.py
import turtle as trtl

# create ladybug head
spider = trtl.Turtle()

legs = 6
#number of spider legs

leg_length = 70
#length of the legs

leg_angle = 360 / legs
#angle between the legs

spider.pensize(5)
#Thickness of the legs
spider_space = 0
while (spider_space < legs):
  spider.goto(0,-28)
  spider.setheading(leg_angle*spider_space)
  spider.forward(leg_length)
  spider_space = spider_space+1

ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(0, -55)
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
for num in range(2):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 10, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)
  xpos = ypos + 65
  ypos = ypos + 20
  num_dot = num_dots + 1


  # position next dots

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()
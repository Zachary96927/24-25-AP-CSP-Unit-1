#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)

legs = 8
#number of spider legs

leg_length = 70
#length of the legs

leg_angle = 360 / legs
#angle between the legs

spider.pensize(5)
#Thickness of the legs
spider_space = 0
while (spider_space < legs):
  spider.goto(0,20)
  spider.setheading(leg_angle*spider_space)
  spider.forward(leg_length)
  spider_space = spider_space+1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()
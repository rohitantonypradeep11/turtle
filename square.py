import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(400,300)
p = turtle.Turtle()
for i in range(4):
    p.forward(100)
    p.left(90)
    i = i+1
turtle.done()
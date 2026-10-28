import turtle

t = turtle.Turtle()
t.pensize(10)

def sectorSwapColor(color1, color2, segmentCount, i):
    if int(i / (360 / segmentCount)) % 2 == 0:
        t.color(color1)
    else:
        t.color(color2)

# for i in range(360):
#     t.forward(1)
#     t.right(1)
#     sectorSwapColor("green", "cyan", 8, i)

t.forward(100)
t.goto(100, 200)

t.right(190)
t.color("red")
t.pensize(45)
t.back(100)

# while t.xcor() < 300:
#     t.forward(1)
#     if t.xcor() > 150:
#         t.color("red")
#     else:
#         t.color("blue")

turtle.done()
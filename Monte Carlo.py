import random
import turtle

turtle.tracer(0, 0)
t = turtle.Turtle()
t.goto(0, 0)
t.pensize(3)
t.screen.bgcolor("black")
t.color("white")
t.circle(150)
t.fd(150)
for x in range(0, 4):
    t.left(90)
    t.fd(300)
turtle.update()
t.up()
x = 0
y = 0
pi = 0
count = 0
while count != 10000:
    count = count + 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x * x + y * y <= 1:
        pi = pi + 1
        t.goto(x * 150, y * 150 + 150)
        t.down()
        t.color("blue")
        t.dot()
        t.up()
    else:
        t.goto(x * 150, y * 150 + 150)
        t.down()
        t.color("red")
        t.dot()
        t.up()
pi = (pi / count) * 4
print(pi)
input("Press Enter key to end: ")
turtle.update()

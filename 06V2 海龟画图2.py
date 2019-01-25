import turtle

turtle.screensize(100,100,"white")
t=turtle.Pen()
t.pencolor("red")
t.pensize(3)
t.speed(5)
tim=1
a=3
while tim<=100:
    print (tim)
    t.forward(a)
    a=a+3
    t.right(89)
    tim=tim+1

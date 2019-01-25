import turtle

turtle.screensize(400,400,"white")
t=turtle.Pen()
t.pencolor("blue")
t.pensize(5)
t.speed(5)

tim=1
a=5
while tim<=30:
    print (tim)
    t.forward(a)
    a=a+5
    t.left(90)
    tim=tim+1
    

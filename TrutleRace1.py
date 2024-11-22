import random
from turtle import Turtle

t1 = Turtle()
t2 = Turtle()
Linie = Turtle()

#Start und Ziel Linie
Linie.penup()
Linie.goto(-100,100)
Linie.right(90)
Linie.pendown()
Linie.forward(200)
Linie.penup()
Linie.goto(100,100)
Linie.pendown()
Linie.forward(200)

#Infinite Turtle Race
while True:
    t1.penup()
    t2.penup()
    t1.goto(-100,10)
    t2.goto(-100,-10)


    while(t1.xcor()<100 or t2.xcor()<100):
        t1.speed("slow")
        t2.speed("slow")
        r1 = random.randint(1,10)
        r2 = random.randint(1,10)
        t1.forward(r1)
        t2.forward(r2)
    if t1.xcor() > t2.xcor():
        print("Turtle 1 has won!")
    else:
        print("Turtle 2 has won!")
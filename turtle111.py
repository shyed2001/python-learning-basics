print("import command packages")
print("import turtle command drawing package, there are many pakages")

print("turtle V 1.12.2")

import turtle
x=(input("Please enter the desired BG color  :    "))
print("# allows us to use turtle")
wn = turtle.Screen()
print("#Creates a playground for turtle. Not must?")
tut=turtle.Turtle()
print("# Creates aturtle, assign to tut")
tut.pen()
wn.title("first turtle")
wn.bgcolor(x)
wn.title("First turtle")
print("Above, Not must necessary")
tut.forward(200)
tut.back(120)
tut.pensize(7)
tut.left(200)
tut.color("yellow")
tut.back(120)
tut.pensize(7)
tut.forward(20)
tut.left(20)
tut.forward(120)
tut.back(120)
tut.right(20)
ooo=(input("Please enter the desired color  :    "))
tut.color(ooo)
tut.forward(120)
tut.left(20)
tut.forward(120)
xx=(input("Please enter the desired pensize  :    "))
tut.pensize(xx)
tut.right(20)
tut.color("blue")
tut.forward(120)
yy=int((input("Please enter the desired pensize  :    ")))
tut.pensize(yy)
tut.right(20)
tut.back(120)
tut.right(20)
tut = wn.mainloop()
print(""" Work 'tut = wn.mainloop()' necessary, this makes the
 program to wait for the user to close window""")


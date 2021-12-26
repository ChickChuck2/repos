import turtle

wn = turtle.Screen()

wn.bgcolor("light green")
wn.title("Turtle")

skk = turtle.Turtle()

def k1():
    skk.right(90)

def k2():
    skk.left(90)

def k3():
    skk.left(180)
def k4():
    skk.right(180)

def RUN():
    skk.forward(90)

def k5():
    skk.left(5)

def k6():
    skk.right(5)

def undo():
    skk.undo()


wn.onkey(k3, "w")
wn.onkey(k2, "a")
wn.onkey(k4, "s")
wn.onkey(k1, "d")
wn.onkey(k5, "q")
wn.onkey(k6, "e")
wn.onkey(undo, "z")

wn.onkey(RUN, "space")

turtle.listen()
turtle.mainloop()
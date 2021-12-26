import turtle

wn = turtle.Screen()

wn.bgcolor("light green")
wn.title("Turtle")

skk = turtle.Turtle()

for i in range(90):
    skk.left(70)
    skk.forward(65)
    skk.clone()
    skk.color("green")

    skk.circle(20)

    skk.fillcolor("red")
    skk.left(0)
    skk.speed(5)


turtle.mainloop()
import turtle




screen = turtle.Screen()


screen.setup(800, 800)


screen.bgcolor('pink')
t = turtle.Turtle()
t.showturtle()
t2 = turtle.Turtle()
t2.showturtle()
t3 = turtle.Turtle()
t3.showturtle()
t3.hideturtle()


t.hideturtle()
t2.hideturtle()


t.speed(2000)
t.penup()



t2.penup()
t2.goto(0, 100)
t2.pendown()
t3.penup()
t3.goto(0, 200)
t.penup()
t.goto(0, 50)
t.pendown()
t.write("All About Me", font=("arial", 30, "bold"), align="center")
t.penup()
t.goto(-50,100)
t.pendown()
t.fillcolor("purple")
t.begin_fill()
t.goto(50,100)
t.goto(0,200)
t.goto(-50,100)
t.end_fill()
t.penup()
t.goto(-225,0)
t.penup()
t.goto(0, -50)
t.pendown()
t.write("Malak Bououdina", font=("arial", 30, "bold"), align="center")
enter = input("press enter to begin")
t.showturtle()
t.clear()
t.penup()
t.goto(150,0)
t.pendown()
t.fillcolor('yellow')
t.begin_fill()
t.setheading(45)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()


t.penup()
t.goto(-300,0)
t.pendown()
t.fillcolor('green')
t.begin_fill()
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()
t.setheading(0)

t.penup()
t.goto(0,-225)
t.pendown()
t.fillcolor('cornsilk')
t.begin_fill()



t.penup()
t.goto(0,250)
t.write("My favorite food", font=("arial", 30, "bold"), align="center")



turtle.addshape("pizza.gif")
t.shape("pizza.gif")
t.goto(150,150)
a = t.stamp()
t.hideturtle()
t.goto(150,200)
t.write("Pizza", font=("arial", 30, "bold"), align="center")


turtle.addshape("Noodles.gif")
t.shape("Noodles.gif")
t.goto(0,0)
b = t.stamp()
t.goto(0,50)
t.write("Pizza", font=("arial", 30, "bold"), align="center")
turtle.addshape("macandcheese.gif")
t.shape("macandcheese.gif")
t.goto(-300,200)
c = t.stamp()
t.goto(0,0)
t.goto(-250,200)
t.write("macandcheese", font=("arial", 30, "bold"), align="center")
enter = input("press enter to begin")
t.clear()
t.clearstamps()

t.penup()
t.goto(0,300)
t.write("My favorite hobbies", font=("arial", 30, "bold"), align="center")


turtle.addshape("lax.gif")
t.shape("lax.gif")
t.goto(150,150)
a = t.stamp()
t.hideturtle()
t.goto(150,200)
t.write("Lacrosse", font=("arial", 30, "bold"), align="center")


turtle.addshape("running.gif")
t.shape("running.gif")
t.goto(0,0)
b = t.stamp()
t.goto(0,50)
t.write("running", font=("arial", 30, "bold"), align="center")
turtle.addshape("reading.gif")
t.shape("reading.gif")
t.goto(0,-150)
c = t.stamp()
t.goto(0,0)
t.goto(0,-100)
t.write("reading", font=("arial", 30, "bold"), align="center")

t.pendown()
t.fillcolor("gray")
t.begin_fill()
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()

enter = input("press enter to begin")

t.clear()

t.penup()
t.goto(0,300)
t.write("My favorite movie", font=("arial", 30, "bold"), align="center")

t.goto(100,100)
t.setheading(90)
t.begin_fill()
t.circle(30)
t.end_fill()




t.goto(-100,100)
turtle.addshape("mammamia.gif")
t.shape("mammamia.gif")
t.goto(0,-150)
c = t.stamp()
t.goto(0,0)
t.goto(0,-100)
t.write("mammia mia", font=("arial", 30, "bold"), align="center")



t.goto(100,-100)
turtle.addshape("littlewomen.gif")
t.shape("littlewomen.gif")
t.goto(0,0)
b = t.stamp()
t.goto(0,50)
t.write("Little Women", font=("arial", 30, "bold"), align="center")
enter = input("press enter to begin")

t.clear()
t.goto(0,300)
t.penup()
t.write("My favorite sport", font=("arial", 30, "bold"), align="center")
turtle.addshape("lax.gif")
t.shape("lax.gif")
t.goto(0,-150)
c = t.stamp()
t.goto(0,0)
t.goto(0,-100)
t.write("lacrosse", font=("arial", 30, "bold"), align="center")



t.goto(100,100)
turtle.addshape("lax2.gif")
t.shape("lax2.gif")
t.goto(0,0)
b = t.stamp()
t.goto(0,50)
t.write("lacrosse", font=("arial", 30, "bold"), align="center")
t.penup()
t.goto(150,-200)
t.pendown()
t.fillcolor('red')
t.begin_fill()
t.setheading(45)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.setheading(0)
t.end_fill()
turtle.done()
enter = input("press enter to begin")


turtle.done()
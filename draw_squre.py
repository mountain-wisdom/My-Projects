import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("white")
    print("window is finished")
    brad = turtle.Turtle()
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    print("turtle is finished")
    window.exitonclick()

draw_square()

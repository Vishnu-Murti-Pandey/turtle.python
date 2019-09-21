import turtle

my_turtle=turtle.Turtle()

def game(length,angle):#formal arguments

    for i in range(0,8):
        my_turtle.forward(length)
        my_turtle.left(angle)
        my_turtle.forward(length)
        my_turtle.left(angle)
        my_turtle.forward(length)
        my_turtle.left(angle)
        my_turtle.forward(length)
        my_turtle.left(angle)
        my_turtle.forward(length)
        my_turtle.left(angle)
        my_turtle.forward(length)
        my_turtle.left(angle)
        my_turtle.forward(length)
        my_turtle.left(angle)
        my_turtle.forward(length)

game(100,45)#actual arguments



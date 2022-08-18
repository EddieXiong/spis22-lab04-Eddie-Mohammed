import turtle
turtle.right(270)
def tree(trunk_length, height):
    if height < 10:
        return
    turtle.forward(height)
    turtle.left(30)
    tree(trunk_length, height * 0.6)
    turtle.right(60)
    tree(trunk_length, height * 0.6)
    turtle.left(30) 
    turtle.back(height)

    turtle.speed("slowest")
tree(200, 20)
turtle.done
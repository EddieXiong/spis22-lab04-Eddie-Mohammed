import turtle

def spiral(initial_length, angle, multiplier) :
    turtle.forward (initial_length) 
    turtle.right (angle)
    spiral(initial_length*multiplier, angle, multiplier)
#spiral(100, 90, 0.9)
spiral(1,-45,1.1)
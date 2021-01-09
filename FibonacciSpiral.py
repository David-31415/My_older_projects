import turtle


fibonacci_number=int(input("How many squares?"))

for i in range(fibonacci_number):
    first=0
    second=1
    temporarysecond=1
    sequence=[]
    for i in range(fibonacci_number):
        temporarysecond=second
        second=first+second
        first=temporarysecond
        sequence.append(first)

print(sequence)

def draw_square(size):
    turtle.speed(10)
    for i in range(5):
        turtle.forward(size)
        turtle.left(90)
    turtle.forward(size)
    turtle.dot(5)

for i in range((fibonacci_number)):
    draw_square(4*sequence[i])

turtle.penup()
turtle.setpos(0,0)
turtle.pendown()
turtle.colormode(255)
turtle.pencolor((212,175,55))
turtle.setheading(0)
turtle.pensize(5)

for i in range((fibonacci_number)):
    turtle.circle(4*sequence[i],90)
    

def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

#length = float(input("Enter the length of the rectangle: "))
#width = float(input("Enter the width of the rectangle: "))

#perimeter = calculate_perimeter(length, width)

#print(f"The perimeter of the rectangle is: {perimeter}")


def calculate_area(base, height):
    area = 0.5 * base * height
    return area
# Input the base and height of the triangle
#base = float(input("Enter the base of the triangle: "))
#height = float(input("Enter the height of the triangle: "))

# Calculate the area
#area = calculate_area(base, height)

# Output the result
#print(f"The area of the triangle is: {area}")


import turtle

# Function to draw a petal
def draw_petal():
    turtle.circle(100, 60)
    turtle.left(120)
    turtle.circle(100, 60)
    turtle.left(120)

# Setup turtle
#turtle.speed(10)  # Set the speed of the turtle
turtle.bgcolor("white")  # Set background color

# Draw flower with multiple petals
turtle.color("red")  # Petal color
for _ in range(6):
    draw_petal()
    turtle.right(60)

# Draw flower center
#turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.color("yellow")
turtle.circle(50)  # Draw the circle at the center of the flower

# Hide turtle and display the result
turtle.hideturtle()
#turtle.done()


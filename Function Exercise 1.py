#Function to get Area of Rectangle
#Defining the function
def areaOfRectangle():
    length = int(input("Enter Length:\n"))
    width = int(input("Enter Width:\n"))
    area = length*width
    print("Area of Rectangle is: " , area , "cm squared")
          
#Outside of function
#Here, we CALL the function
areaOfRectangle()

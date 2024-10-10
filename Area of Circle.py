#Function to get Area of Circle
import math
#Defining the function
def areaOfCircle():
    #Pi= int(3.14)
    Radius = int(input("Enter radius:\n"))
    area = math.pi*Radius*Radius
    print("Area of Circle is: " , area , "cm squared")
          
#Outside of function
#Here, we CALL the function
areaOfCircle()

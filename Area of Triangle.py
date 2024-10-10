#Function to get Area of Circle
#Defining the function
def areaOfTriangle():
    half= int(0.5)
    Base = int(input("Enter base:\n"))
    Height = int(input ("Enter height: \n"))
    area = half*Base*Height
    print("Area of Triangle is: " , area , "cm squared")
          
#Outside of function
#Here, we CALL the function
areaOfTriangle()
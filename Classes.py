#CReate a Class called Area
#This class wil contain all the
#--functions to calculate Area

import math
class area:
        #Create a Constructor
        #This is a function also refered to
        #as__init__
        #def __init__(self,l,w,r):
            self.length = l
            self.width = w
            self.Radius = r
                     
         
        def areaOfRectangle(self):
            length = int(input("Enter Length:\n"))
            width = int(input("Enter Width:\n"))
            area = self.length*self.width


        def areaOfCircle(self):
            Pi= int(3.14)
            Radius = int(input("Enter radius:\n"))
            area = math.pi*self.Radius*self.Radius
        
        def TriArea():
            Base = int()
            Height = int()
            Half = (1/2)
            area =Base*Height*Half
            print("Area of Triangle is: " , area , "cm squared")
        
        def TriArea(self):
            Base = int(input("Enter Length:\n"))
            Height = int(input("Enter Width:\n"))
            Half = int(1/2)
            area = self.Base*self.Height/self.half
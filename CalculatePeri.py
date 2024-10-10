from PerimeterClass import Perimeter

choice = int(input("Enter 1,2 or 3:\n")) 

if choice == 1:
    l = int(input("Enter length:\n"))
    w = int(input("Enter width:\n"))
    RObj=Perimeter(l,w,0)
    RObj.PerimeterOfRectangle()

elif choice == 2:
    r = int(input("Enter Radius: \n"))
    RObj=Perimeter(0,0,r)
    RObj.Circumf()

elif choice == 3:
    l = int(input("Enter length:\n"))
    RObj=Perimeter(l,0,0)
    RObj.PeriTri()

else:
    print("Invalid Choice")
import math
class Perimeter:
    def __init__(self, l, w, r):
        self.length = l
        self.width = w
        self.radius = r

    def PerimeterOfRectangle(self):
        Perimeter = self.length + self.length + self.width + self.width
        print("PerimeterOfRectangle is:", Perimeter, "cm squared")

    def Circumf(self):
        Perimeter = math.pi * 2 * self.radius
        print("CircumferenceOfCircle is:", Perimeter, "cm squared")
        
    def PeriTri(self):
        Perimeter = self.length + self.length + self.length
        print("PerimeterofTriangle is:", Perimeter,"cm squared")
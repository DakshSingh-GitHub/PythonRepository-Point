
class NotAnInstanceError(Exception):
    """NotAnInstanceError: User Defined
    - This class raises an exception (error) if the function's semantics aren't correct
    - in the point class, the parameters cannot be string or boolean, so it rises an error"""
    
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class point(object):
    BASE = "point"
    TYPE = "compound_type"
    COMPATIBILITY = "universal"

    """[WAIT FOR THE UPDATED DRAFT]
    Point Class for denoting a point to a variable:
    this class has a total of 8 method excluding the constructor:
    1 method - constructor (__init__)
    2 methods (getX, getY) are getters
    2 methods (updateX, updateY) are setter
    1 methods (distanceBetweenPoints) for calculating the distance between X and Y axis
    1 method (Quadrant) for to tell which quadrant point is in
    2 method (getDocumentation, getInstanceInfo)
    2 method (__str__, __add__) magic methods"""

    def __init__(self, x=0, y=0) -> None:
        if isinstance(x, int) and isinstance(y, int):
            self.Xcoord = x
            self.Ycoord = y

        elif isinstance(x, float) and isinstance(y, float):
            if y == int(y) and x == int(x):
                self.Xcoord = int(x)
                self.Ycoord = int(y)
            else:
                self.Xcoord = x
                self.Ycoord = y
            
        elif isinstance(x, float) and isinstance(y, int):
            if x == int(x):
                self.Xcoord = x
                self.Ycoord = int(y)
            else:
                self.Xcoord = x
                self.Ycoord = float(y)

        elif isinstance(x, int) and isinstance(y, float):
            if y == int(y):
                self.Xcoord = x
                self.Ycoord = int(y)
            else:
                self.Xcoord = float(x)
                self.Ycoord = y

        else:
            raise NotAnInstanceError("values given are not an instance of 'float' or 'int'")
        
    # getters
    # to get the values of X and Y coordinates
    def getX(self):
        """To get the alue of Y"""
        return self.Xcoord
    
    def getY(self):
        """To get the value of Y"""
        return self.Ycoord
    
    # setters
    def updateX(self, newVal):
        """It updates the X coordinate while also looking out for other value:
        - if the other value is n.0, and the given value is p, so the point will be (n, p)
        - if the other value is n, and the given value is p.q, so the point will be (n.0, p.q)
        - if the other value is p.q, and the given value is n.m, point will be (p.q, n.m)
        - check the rest by testing"""
        if isinstance(newVal, int):
            if isinstance(self.Ycoord, int):
                self.Ycoord = int(self.Ycoord)
                self.Xcoord = int(newVal)
            elif isinstance(self.Ycoord, float):
                if self.Ycoord > int(self.Ycoord) and self.Ycoord < (int(self.Ycoord)+1):
                    self.Ycoord = self.Ycoord
                    self.Xcoord = float(newVal)
                else:
                    self.Ycoord = int(self.Ycoord)
                    self.Xcoord = newVal

        elif isinstance(newVal, float):
            if newVal > int(newVal) and newVal < (int(newVal)+1):
                self.Ycoord = float(self.Ycoord)
                self.Xcoord = newVal
            
            else:
                if self.Ycoord > int(self.Ycoord) and self.Ycoord < int(self.Ycoord)+1:
                    self.Ycoord = self.Ycoord
                    self.Xcoord = float(newVal)
                else:
                    self.Ycoord = int(self.Ycoord)
                    self.Xcoord = int(newVal)

        else:
            raise NotAnInstanceError("new value should be a instance of 'float' or 'int'")

    def updateY(self, newVal):
        """It updates the Y coordinate while also looking out for other value:
        - if the other value is n.0, and the given value is p, so the point will be (p, n)
        - if the other value is n, and the given value is p.q, so the point will be (p.q, n.0)
        - if the other value is p.q, and the given value is n.m, point will be (n.m, p.q)
        - check the rest by testing"""
        if isinstance(newVal, int):
            if isinstance(self.Xcoord, int):
                self.Xcoord = self.Xcoord
                self.Ycoord = newVal
            elif isinstance(self.Xcoord, float):
                if self.Xcoord > int(self.Xcoord) and self.Xcoord < (int(self.Xcoord)+1):
                    self.Xcoord = self.Xcoord
                    self.Ycoord = float(newVal)
                else:                                # number is a perfect integer
                    self.Xcoord = int(self.Xcoord)
                    self.Ycoord = newVal

        elif isinstance(newVal, float):
            if newVal > int(newVal) and newVal < (int(newVal)+1):
                self.Xcoord = float(self.Xcoord)
                self.Ycoord = newVal
            
            else:
                if self.Xcoord > int(self.Xcoord) and self.Xcoord < int(self.Xcoord)+1:
                    self.Xcoord = self.Xcoord
                    self.Ycoord = float(newVal)
                else:
                    self.Xcoord = int(self.Xcoord)
                    self.Ycoord = int(newVal)
            
        else:
            raise NotAnInstanceError("new value should be a instance of 'float' or 'int'")     

    # instance methods
    def Quadrant(self):
        """This function tells in which quadrant the given point is in"""
        if self.Xcoord == 0 and self.Ycoord == 0:
            return "Center"
        elif self.Xcoord > 0 and self.Ycoord > 0:
            return "First Quadrant"
        elif self.Xcoord < 0 and self.Ycoord < 0:
            return "Third Quadrant"
        elif self.Xcoord < 0 and self.Ycoord > 0:
            return "Second Quadrant"
        elif self.Xcoord > 0 and self.Ycoord < 0:
            return "Fourth Quadrant"
        else:
            pass

    def DistanceBetweenPoint(self, other):
        """This function is going to calculate the distance between teo points by calculating the hypotenuse"""
        def hypotenuse(perpendicular, base):
            import math
            sumOfSquare = (perpendicular**2) + (base**2)
            hyp = math.sqrt(sumOfSquare)
            return hyp

        if isinstance(other, point):
            if self.Ycoord > other.Ycoord:
                if self.Xcoord < other.Xcoord:
                    self, other = other, self
                elif self.Xcoord > other.Xcoord:
                    pass
                perpendicular = self.Ycoord - other.Ycoord
                base = self.Xcoord - other.Xcoord
                res = hypotenuse(perpendicular=perpendicular, base=base)
                return res
            elif self.Ycoord < other.Ycoord:
                if self.Xcoord < other.Xcoord:
                    self, other = other, self
                elif self.Xcoord > other.Xcoord:
                    pass
                base = other.Xcoord - self.Xcoord
                perpendicular = other.Ycoord - self.Ycoord
                res = hypotenuse(perpendicular=perpendicular, base=base)
                return res
            else:
                return 0
        
        else:
            raise NotAnInstanceError("values given are not an instance of 'float' or 'int'")

    # magic methods
    def __str__(self) -> str:
        """USER-DEFINED:
        -To get the values by: print(<instance name>)"""
        finstr = f"({self.Xcoord}, {self.Ycoord})"
        return finstr
    
    def __add__(self, other):
        """USER-DEFINED:
        -To add the points on both points"""
        if isinstance(other, point):
            Fp = self.Xcoord + other.Xcoord
            Sp = self.Ycoord + other.Ycoord
            p3 = point(Fp, Sp)
            return p3
        else:
            raise NotAnInstanceError("values given are not an instance of 'float' or 'int'")

    @classmethod
    def getInstanceInfo(cls):
       return f"class: {point.BASE}\ntype: {point.TYPE}\ncompatibility: {point.COMPATIBILITY}"
       
    @classmethod
    def getDocumentation(cls):
        return point.__doc__

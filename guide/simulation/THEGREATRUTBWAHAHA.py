"""
https://usaco.org/index.php?page=viewproblem2&cpid=1061 
Andrew
"""

class Vector():
    def __init__(self, inx, iny):
        self.x = inx
        self.y = iny

    def __mul__(self, other: float) -> "Vector":
        return Vector(self.x * other, self.y * other)
    
    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)
    
    def __eq__(self, value: "Vector") -> "Vector":
        return (value.x == self.x and value.y == self.y)

    def magnitude() -> float:
        return pow((pow() + ))
            

class Cow:
    def __init__ (self, x: int,y: int, dir: str):
        self.pos = Vector(x,y)
        if dir == "E":
            self.dir = Vector(1,0)
        elif dir == "W":
            self.dir = Vector(-1,0)
        elif dir == "N":
            self.dir = Vector(0, 1)
        elif dir == "S":
            self.dir = Vector(0, -1)
    
    def checkForCollisions(cow1: "Cow", cow2: "Cow") -> "Vector":
        dirsum = cow1.dir + cow2.dir
# take input
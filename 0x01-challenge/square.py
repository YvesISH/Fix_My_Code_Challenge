#!/usr/bin/python3

class Square():
    
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """Area of the square."""
        return self.width * self.height

    def perimeter(self):
        """Perimeter of the square."""
        return 2 * (self.width + self.height)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter())

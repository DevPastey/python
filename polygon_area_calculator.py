class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def __repr__(self):
        return self.__str__()


    def set_width(self, value):
        self.width = value

    def set_height(self, value):
        self.height = value
    
    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter
    
    def get_diagonal(self):
        diagonal = ( (self.width**2) + (self.height**2) )**0.5
        return diagonal 
    
    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return("Too big for picture.")
        row = f"{'*' * self.width}\n"
        return(row * self.height)
    

    def get_amount_inside(self, shape):
        width_fit = self.width // shape.width 
        height_fit = self.height // shape.height 
        return (width_fit * height_fit)


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def set_width(self, value):
        self.width = value
        self.height = value

    def set_height(self, value):
        self.height = value
        self.width = value
    

    def set_side(self, value):
        self.height = value
        self.width = value

    def __str__(self):
        return f"Square(side={self.width})"
    

    def __repr__(self):
        return self.__str__()

    def get_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
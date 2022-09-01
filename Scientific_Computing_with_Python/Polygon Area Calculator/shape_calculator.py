class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        description = "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
        return description

    def set_width(self, input_widht):
        self.width = input_widht

    def set_height(self, input_height):
        self.height = input_height

    def get_area(self):
        area = self.height * self.width
        return area

    def get_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self):
        picture = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            for i in range(self.height):
                picture += "*" * self.width + '\n'
        return picture

    def get_amount_inside(self, shape):
        num = self.get_area() / shape.get_area()
        return int(num)



class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        # Rectangle.__init__(self, side, side)
        # self.width = side
        # self.height = side

    def __str__(self):
        description = "Square(side=" + str(self.width) + ")"
        return description


    def set_side(self, input_side):
        self.side = input_side
        self.width = input_side
        self.height = input_side

from math import radians, tan


class StraightLine:

    def __init__(self, x=None, y=None, ang=None, k=None, b=None):

        self.typeOfLine = 0

        if (x is not None) and (y is not None) and (ang is not None):
            self.x, self.y, self.ang, self.typeOfLine = x, y, ang, 1
        elif (k is not None) and (b is not None):
            self.k, self.b, self.typeOfLine = k, b, 2

    def equation(self):
        if self.typeOfLine > 0:
            self.find_koef()
            return f'y = {self.k}*x + {self.b}'

    def find_y(self, x: float):
        if self.typeOfLine > 0:
            self.find_koef()
            return self.k * x + self.b

    def find_koef(self):
        if self.typeOfLine == 1:
            self.k = tan(radians(90 + self.ang))
            self.b = self.y - self.k * self.x
            self.typeOfLine = 2


def find_fortress(line1: StraightLine, line2: StraightLine):
    x_res = (line2.b - line1.b) / (line1.k - line2.k)
    y_res = line1.k * x_res + line1.b
    return x_res, y_res

# Define coordinates and angle of ender eye two-times throwing
x1, z1, ang1 =  -77.733, -1623.702,  141.5
x2, z2, ang2 = -894.546, -1644.208, -131.0

l1 = StraightLine(x=x1, y=z1, ang=ang1)
l2 = StraightLine(x=x2, y=z2, ang=ang2)

# print(f'{l1.equation()}\n{l2.equation()}')
print(f'{find_fortress(l1, l2)}')

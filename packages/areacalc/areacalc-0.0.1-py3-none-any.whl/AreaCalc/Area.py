""" Library includes class with methods, which calculate areas of figures """

from math import pi, tan, sqrt


class Area:
    """ Class for calculating the areas of figures """

    @staticmethod
    def circle_radius(r: float):
        """ Returns area of the circle using radius of the circle """
        if r < 0:
            raise ValueError("Radius must be >= 0")
        return r * r * pi

    @staticmethod
    def triangle_sides(a: float, b: float, c: float):
        """ Returns area of the triangle using length of each side of the triangle """
        if any(x < 0 for x in [a, b, c]):
            raise ValueError("Sides of the triangle must be > 0")
        p = (a + b + c) / 2
        ar = sqrt(p * (p - a) * (p - b) * (p - c))
        a, b, c = sorted([a, b, c])
        if (a*a + b*b) == c*c:
            print("Triangle is rectangular!")
        return ar

    @staticmethod
    def square_side(a: float):
        """ Returns area of the square using length of the side of the square """
        if a <= 0:
            raise ValueError("Sides of the square must be > 0")
        return a * a

    @staticmethod
    def rectangle_sides(a: float, b: float):
        """ Returns area of the rectangle using length of the side of the rectangle """
        if any(x < 0 for x in [a, b]):
            raise ValueError("Sides of the rectangle must be > 0")
        return a * b

    @staticmethod
    def regular_polygon(side_length: float, num_sides: int):
        """ Returns area of the regular polygon using length of the side and quantity of the sides"""
        if side_length <= 0:
            raise ValueError("Length of sides of the polygon must be > 0")
        elif num_sides < 3:
            raise ValueError("Quantity of sides must be > 2")
        area = (num_sides * side_length * side_length) / (4 * tan(pi / num_sides))
        return area

    @staticmethod
    def polygon_dots(dots: list[(float, float)]):
        """ Returns area of the simple polygon using list of tuple of dots coordinates -> (x,y) (Gauss theorem) """
        area = 0
        last = len(dots) - 1
        for i in range(len(dots)):
            area += dots[last][0] * dots[i][1] - dots[last][1] * dots[i][0]
            last = i
        return 0.5 * abs(area)

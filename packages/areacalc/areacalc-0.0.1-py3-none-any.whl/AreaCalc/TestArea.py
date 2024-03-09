import unittest
from math import pi
from Area import Area


class TestArea(unittest.TestCase):
    def setUp(self) -> None:
        self.area = Area

    def test_circle_radius(self):
        self.assertAlmostEqual(self.area.circle_radius(5), 25 * pi, places=4)

    def test_circle_radius_negative(self):
        with self.assertRaises(ValueError):
            self.area.circle_radius(-5)

    def test_triangle_sides(self):
        self.assertAlmostEqual(self.area.triangle_sides(3,4,5), 6, places=4)

    def test_triangle_sides_negative(self):
        with self.assertRaises(ValueError):
            self.area.triangle_sides(-1, 2, 3)
        with self.assertRaises(ValueError):
            self.area.triangle_sides(1, -2, 3)
        with self.assertRaises(ValueError):
            self.area.triangle_sides(1, 2, -3)
        with self.assertRaises(ValueError):
            self.area.triangle_sides(-1, -2, 3)
        with self.assertRaises(ValueError):
            self.area.triangle_sides(1, -2, -3)
        with self.assertRaises(ValueError):
            self.area.triangle_sides(-1, 2, -3)
        with self.assertRaises(ValueError):
            self.area.triangle_sides(-1, -2, -3)

    def test_square_side(self):
        self.assertAlmostEqual(self.area.square_side(5), 25, places=4)

    def test_square_side_negative(self):
        with self.assertRaises(ValueError):
            self.area.square_side(-5)

    def test_rectangle_sides(self):
        self.assertAlmostEqual(self.area.rectangle_sides(2, 3), 6, places=4)

    def test_rectangle_sides_negative(self):
        with self.assertRaises(ValueError):
            self.area.rectangle_sides(-1, 2)
        with self.assertRaises(ValueError):
            self.area.rectangle_sides(1, -2)
        with self.assertRaises(ValueError):
            self.area.rectangle_sides(-1, -2)

    def test_regular_polygon(self):
        self.assertAlmostEqual(self.area.regular_polygon(3, 4), 9, places=4)

    def test_regular_polygon_negative(self):
        with self.assertRaises(ValueError):
            self.area.regular_polygon(-1, 4)
        with self.assertRaises(ValueError):
            self.area.regular_polygon(3, 2)
        with self.assertRaises(ValueError):
            self.area.regular_polygon(-1, 2)


if __name__ == "__main__":
  unittest.main()
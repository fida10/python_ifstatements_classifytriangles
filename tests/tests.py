import unittest
from src.ans import classify_triangle


class TestClassifyTriangle(unittest.TestCase):
    def test_equilateral_triangle(self):
        self.assertEqual(classify_triangle(3, 3, 3), 'Equilateral')

    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle(5, 5, 3), 'Isosceles')

    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle(4, 5, 6), 'Scalene')

    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), 'Not a triangle')

    def test_invalid_sides(self):
        self.assertEqual(classify_triangle(-1, 2, 3), 'Not a triangle')


if __name__ == '__main__':
    unittest.main()

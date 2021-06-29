import unittest
import Area


class UnitTest_Area(unittest.TestCase):
    def run_test(self):
        area = Area.Area()
        side = int(input("Enter the value of a side: "))
        assert area.area_square(side) == side*side
        radius = int(input("Enter the value of radius of the circle: "))
        if radius > 0:
            radius_positive = True
        else:
            radius_positive = False
        self.assertTrue(radius_positive, "The value of radius should be greater than zero.")
        self.assertNotEqual(area.area_rectangle(6, 8), 48)
        self.assertEqual(area.area_parallelogram(2, 3), 6)

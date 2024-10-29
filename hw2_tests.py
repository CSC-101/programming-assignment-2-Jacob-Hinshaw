import data
import hw2
import unittest

from data import Rectangle, Point


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test1_create_rectangle(self):
        input1 = data.Point(10,2)
        input2 = data.Point(2,10)
        result = hw2.create_rectangle(input1, input2)
        expected = data.Rectangle(input2, input1)
        self.assertEqual(expected, result)
    def test2_create_rectangle(self):
        input1 = data.Point(2,2)
        input2 = data.Point(10,10)
        result = hw2.create_rectangle(input1, input2)
        expected = Rectangle(Point(2,10), Point(10,2))
        self.assertEqual(expected, result)



    # Part 2


    # Part 3


    # Part 4


    # Part 5


    # Part 6





if __name__ == '__main__':
    unittest.main()

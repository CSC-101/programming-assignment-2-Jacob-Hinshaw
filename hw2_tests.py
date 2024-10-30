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
    def test1_shorter_duration_than(self):
        input1 = data.Duration(100, 30)
        input2 = data.Duration(90, 2)
        result = hw2.shorter_duration_than(input1, input2)
        expected = False
        self.assertEqual(expected, result)
    def test2_shorter_duration_than(self):
        input1 = data.Duration(90, 2)
        input2 = data.Duration(90, 2)
        result = hw2.shorter_duration_than(input1, input2)
        expected = False
        self.assertEqual(expected, result)

    # Part 3
    def test1_song_shorter_than(self):
        input1 = [data.Song("Jacob", "Unicycle", data.Duration(90,0)),
                  data.Song("Sophia", "Flute", data.Duration(30,0)),
                  data.Song("Travis", "Soccer", data.Duration(120, 0))]
        input2 = data.Duration(100, 30)
        result = hw2.song_shorter_than(input1, input2)
        expected = [data.Song("Jacob", "Unicycle", data.Duration(90,0)),
                  data.Song("Sophia", "Flute", data.Duration(30,0))]
        self.assertEqual(expected, result)
    def test2_song_shorter_than(self):
        input1 = [data.Song("Jacob", "Unicycle", data.Duration(90,0)),
                  data.Song("Sophia", "Flute", data.Duration(30,0)),
                  data.Song("Travis", "Soccer", data.Duration(120, 0))]
        input2 = data.Duration(20, 30)
        result = hw2.song_shorter_than(input1, input2)
        expected = []
        self.assertEqual(expected, result)

    # Part 4
    def test1_running_time(self):
        input1 = [data.Song("Decemberists", "June Hymn", data.Duration(4,30)),
                  data.Song("Broken Bells", "October", data.Duration(3,40)),
                  data.Song("Kansas", "Dust in the Wind", data.Duration(3,29)),
                  data.Song("Local Natives", "Airplanes", data.Duration(3,58))]
        input2 = [0,2,1,3,0]
        result = hw2.running_time(input1, input2)
        expected = data.Duration(20,7)
        self.assertEqual(expected, result)
    def test2_running_time(self):
        input1 = [data.Song("Decemberists", "June Hymn", data.Duration(4,30)),
                  data.Song("Broken Bells", "October", data.Duration(3,40)),
                  data.Song("Kansas", "Dust in the Wind", data.Duration(3,29)),
                  data.Song("Local Natives", "Airplanes", data.Duration(3,58))]
        input2 = [-1,10,2]
        result = hw2.running_time(input1, input2)
        expected = data.Duration(3,29)
        self.assertEqual(expected, result)
    # Part 5


    # Part 6





if __name__ == '__main__':
    unittest.main()

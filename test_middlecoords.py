import unittest
import middlecoords


class MiddlePositionTests(unittest.TestCase):
    def setUp(self):
        """
        Set up our calculator, default position and expected result
        """

        self.calculator = middlecoords.get_middle_position

        self.first_lat, self.first_long = 50.5000, 30.8000
        self.second_lat, self.second_long = 50.7000, 31.0000
        self.third_lat, self.third_long = 50.7000, 30.8000
        self.fourth_lat, self.fourth_long = 50.5000, 31.0000

        self.middle_position = 50.6000, 30.9000

    def test_between_two_positions(self):
        """
        get_middle_position() should get two positions and calculate the middle position
        """
        result_position = self.calculator(self.first_lat, self.first_long,
                                          self.second_lat, self.second_long, )

        self.assertEqual(result_position, self.middle_position)

    def test_between_four_positions(self):
        """
        get_middle_position() should get positions (no matter how many: 1,2, 4, 256) and calculate middle position
        """
        result_position = self.calculator(self.first_lat, self.first_long,
                                          self.second_lat, self.second_long,
                                          self.third_lat, self.third_long,
                                          self.fourth_lat, self.fourth_long)
        self.assertEqual(result_position, self.middle_position)

    def test_unpaired_position(self):
        """
        get_middle_position() should raise exception if not paired values passed
        """
        self.assertRaises(middlecoords.NoPair,
                          self.calculator,
                          self.first_lat, self.first_long,
                          self.second_lat)


if __name__ == '__main__':
    unittest.main()

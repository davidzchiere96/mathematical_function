import unittest
from unittest.mock import patch, MagicMock
from mathFunction import AverageFunction, input_arguements

class TestAverageFunction(unittest.TestCase):
    @patch('builtins.input', return_value='1 2 3 4 5')
    def test_calculate(self, mock_input):
        average_function = AverageFunction()
        result = average_function.calculate(1, 2, 3, 4, 5)
        self.assertAlmostEqual(result, 3)

    @patch('builtins.input', return_value='1 2 3 4 5')
    def test_input_arguements(self, mock_input):
        result = input_arguements()
        self.assertEqual(result, [1.0, 2.0, 3.0, 4.0, 5.0])

if __name__ == '__main__':
    unittest.main()

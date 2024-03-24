import unittest
from unittest.mock import patch, MagicMock
import main

class TestMain(unittest.TestCase):
    @patch('main.mathFunction.input_arguements', return_value=[1, 2, 3, 4, 5])
    @patch('main.logger.logger')
    def test_main(self, mock_logger, mock_input_arguements):

        result = main.main()

        mock_input_arguements.assert_called_once()
        mock_logger.assert_called_once()

        self.assertAlmostEqual(result, 3.0)

if __name__ == "__main__":
    unittest.main()

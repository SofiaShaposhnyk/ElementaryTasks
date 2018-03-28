import unittest
import CompareSquares
from Triangle import Triangle
from unittest.mock import patch


class TestCompareSquares(unittest.TestCase):
    def test_validate_parameters_valid_value(self):
        actual = CompareSquares.validate_parameters(3, 4, 5)
        self.assertTrue(actual)

    def test_validate_parameters_invalid_value(self):
        actual = CompareSquares.validate_parameters(10, 4, 5)
        self.assertFalse(actual)

    @patch("CompareSquares.input_text", return_value="y")
    def test_continue_input_true(self, input):
        actual = CompareSquares.continue_input()
        self.assertTrue(actual)

    @patch("CompareSquares.input_text", return_value="")
    def test_continue_input_false(self, input):
        actual = CompareSquares.continue_input()
        self.assertFalse(actual)

    @patch("CompareSquares.input_text", return_value="name1, 2.2, 3.3, 4.4")
    def test_input_parameters_valid_value(self, input):
        expected = ("name1", 2.2, 3.3, 4.4)
        actual = CompareSquares.input_parameters()
        self.assertEqual(actual, expected)

    @patch("CompareSquares.input_text", return_value="name1, text, 3.3, 4.4")
    def test_input_parameters_text_value(self, input):
        expected = (False, "Sides parameters should be float.")
        actual = CompareSquares.input_parameters()
        self.assertEqual(actual, expected)

    @patch("CompareSquares.input_text", return_value="name1, 10.5, 3.3, 4.4")
    def test_input_parameters_invalid_value(self, input):
        expected = (False, "Triangle doesn't exist.")
        actual = CompareSquares.input_parameters()
        self.assertEqual(actual, expected)

    @patch("CompareSquares.input_text", return_value="name1, 3.3, 4.4")
    def test_input_parameters_invalid_args(self, input):
        expected = (False, "Enter name snd three sides, separated commas.")
        actual = CompareSquares.input_parameters()
        self.assertEqual(actual, expected)

    def test_triangle_get_square(self):
        tr = Triangle("name1", 22, 22, 22)
        actual = tr.get_square()
        expected = 209.58
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

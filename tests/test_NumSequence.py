import unittest
import NumSequence


class TestNumSequence(unittest.TestCase):
    def test_validation_valid_value(self):
        args = ["file_path", "100"]
        expected = 100
        result = NumSequence.validate(args)
        self.assertEqual(result, expected)

    def test_validation_text_value(self):
        args = ["file_path", "text"]
        expected = "Limit should be integer."
        result = NumSequence.validate(args)
        self.assertEqual(result, expected)

    def test_validation_negative_value(self):
        args = ["file_path", "-10"]
        expected = "Limit should be positive."
        result = NumSequence.validate(args)
        self.assertEqual(result, expected)

    def test_validation_invalid_args(self):
        args = ["file_path"]
        expected = "Enter one number to generate a sequence."
        result = NumSequence.validate(args)
        self.assertEqual(result, expected)

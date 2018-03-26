import unittest
import FibSequence


class TestFibSequence(unittest.TestCase):
    def test_valid_value(self):
        expected = "2, 3, 5, 8, 13, 21, 34, 55, 89"
        result = FibSequence.get_fib_sequence(1, 100)
        self.assertEqual(result, expected)

    def test_negative_value(self):
        args = ["file_path", "-5", "10"]
        expected = "Invalid arguments. Limits should be positive."
        result = FibSequence.validate_args(args)
        self.assertEqual(result, expected)

    def test_text_value(self):
        args = ["file_path", "1", "end"]
        expected = "Invalid arguments. Limits should be integer."
        result = FibSequence.validate_args(args)
        self.assertEqual(result, expected)

    def test_invalid_args(self):
        args = ["file_path", "1", "100", "1000"]
        expected = "Enter two positive limits to generate a sequence."
        result = FibSequence.validate_args(args)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

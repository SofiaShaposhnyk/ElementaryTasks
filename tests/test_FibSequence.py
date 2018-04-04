import unittest
import FibSequence


class TestFibSequence(unittest.TestCase):
    def test_get_fib_sequence_valid_value(self):
        expected = "2, 3, 5, 8, 13, 21, 34, 55, 89"
        result = FibSequence.get_fib_sequence(1, 100)
        self.assertEqual(result, expected)

    def test_validate_args_negative_value(self):
        args = ["-5", "10"]
        expected = False, "Invalid arguments. Limits should be positive."
        result = FibSequence.validate_args(args)
        self.assertEqual(result, expected)

    def test_validate_args_text_value(self):
        args = ["1", "end"]
        expected = False, "Invalid arguments. Limits should be integer."
        result = FibSequence.validate_args(args)
        self.assertEqual(result, expected)

    def test_validate_args_invalid_value(self):
        args = ["1", "100", "1000"]
        expected = False, "Enter two positive limits to generate a sequence."
        result = FibSequence.validate_args(args)
        self.assertEqual(result, expected)

    def test_validate_args_valid_value(self):
        args = ["100", "1000"]
        expected = (100, 1000)
        result = FibSequence.validate_args(args)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

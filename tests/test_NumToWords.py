import unittest
import NumToWords


class TestNumToWords(unittest.TestCase):
    def test_validate_args_valid_value(self):
        args = ["file_path", "9999"]
        expected = (True, "9999")
        actual = NumToWords.validate_args(args)
        self.assertEqual(actual, expected)

    def test_validate_args_text_value(self):
        args = ["file_path", "text"]
        expected = (False, "Enter a number.")
        actual = NumToWords.validate_args(args)
        self.assertEqual(actual, expected)

    def test_validate_args_negative_value(self):
        args = ["file_path", "-100"]
        expected = (False, "Invalid argument. Number should be bigger then 0.")
        actual = NumToWords.validate_args(args)
        self.assertEqual(actual, expected)

    def test_validate_args_without_value(self):
        args = ["file_path"]
        expected = (False, "Enter a number to convert.")
        actual = NumToWords.validate_args(args)
        self.assertEqual(actual, expected)

    def test_get_numeral_valid_value(self):
        expected = 6
        actual = NumToWords.get_numeral(26, 1, 0)
        self.assertEqual(actual, expected)

    def test_get_digits_valid_value(self):
        expected = {"ones": 4, "tens": 1, "hundreds": 5}
        actual = NumToWords.get_digits(514, 0)
        self.assertEqual(actual, expected)

    def test_to_words(self,):
        expected = ["сто", "сорок", "два", ""]
        NumToWords.to_words("142")
        actual = NumToWords.result
        self.assertEqual(expected, actual)

    def test_get_form_valid_ov_value(self):
        digits = {"ones": 4, "tens": 1, "hundreds": 5}
        index = 6
        expected = "миллионов"
        actual = NumToWords.get_form(digits, index)
        self.assertEqual(actual, expected)

    def test_get_form_valid_a_value(self):
        digits = {"ones": 3, "tens": 2, "hundreds": 5}
        index = 9
        expected = "миллиарда"
        actual = NumToWords.get_form(digits, index)
        self.assertEqual(actual, expected)

    def test_get_form_valid_value(self):
        digits = {"ones": 1, "tens": 2, "hundreds": 5}
        index = 9
        expected = "миллиард"
        actual = NumToWords.get_form(digits, index)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

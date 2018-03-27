import unittest
import LuckyTicket
from unittest.mock import patch


class TestLuckyTicket(unittest.TestCase):
    @patch("LuckyTicket.get_input", return_value='LuckyTicketsAlgorithm.txt')
    def test_get_algorithm_name_valid_value(self, input):
        expected = "Moscow"
        result = LuckyTicket.get_algorithm_name()
        self.assertEqual(result, expected)

    @patch("LuckyTicket.get_input", return_value='Wrong.txt')
    def test_get_algorithm_name_invalid_value(self, input):
        self.assertRaises(FileNotFoundError)

    @patch("LuckyTicket.get_input", return_value='6')
    def test_get_number_of_digits_valid_value(self, input):
        expected = 6
        result = LuckyTicket.get_number_of_digits()
        self.assertEqual(result, expected)

    @patch("LuckyTicket.get_input", return_value='text')
    def test_get_number_of_digits_text_value(self, input):
        expected = "Wrong! Number should be integer."
        result = LuckyTicket.get_number_of_digits()
        self.assertEqual(result, expected)

    @patch("LuckyTicket.get_input", return_value='7')
    def test_get_number_of_digits_odd_value(self, input):
        expected = "Wrong! Number should be even, less then 10 and not 0."
        result = LuckyTicket.get_number_of_digits()
        self.assertEqual(result, expected)

    def test_moscow_algorithm_odd_valid_value(self):
        expected = 55252
        result = LuckyTicket.moscow_algorithm(3)
        self.assertEqual(result, expected)

    def test_moscow_algorithm_even_value(self):
        expected = 4816030
        result = LuckyTicket.moscow_algorithm(4)
        self.assertEqual(result, expected)

    def test_choose_algorithm_valid_value(self):
        expected = 55252
        result = LuckyTicket.choose_algorithm("Moscow", 3)
        self.assertEqual(result, expected)

    def test_choose_algorithm_invalid_value(self):
        expected = "Algorithm doesn't exist!"
        result = LuckyTicket.choose_algorithm("New-York", 3)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

import unittest
import Envelops
from unittest.mock import patch


class TestEnvelops(unittest.TestCase):
    def test_is_possible_to_fit_possible_value(self):
        env_1 = {"side1": 9, "side2": 9}
        env_2 = {"side1": 10, "side2": 1}
        result = Envelops.is_possible_to_fit(env_1, env_2)
        self.assertTrue(result)

    def test_is_possible_to_fit_impossible_value(self):
        env_1 = {"side1": 9, "side2": 9}
        env_2 = {"side1": 10, "side2": 8}
        result = Envelops.is_possible_to_fit(env_1, env_2)
        self.assertFalse(result)

    def test_sort_envelops_sort_values(self):
        env_1 = {"side1": 8, "side2": 8}
        env_2 = {"side1": 9, "side2": 9}
        expected = (env_2, env_1)
        result = Envelops.sort_envelops(env_1, env_2)
        self.assertEqual(result, expected)

    def test_sort_envelops_not_sort_values(self):
        env_1 = {"side1": 9, "side2": 9}
        env_2 = {"side1": 8, "side2": 8}
        expected = (env_1, env_2)
        result = Envelops.sort_envelops(env_1, env_2)
        self.assertEqual(result, expected)

    @patch("Envelops.input_text", return_value="10")
    def test_input_parameters_valid_values(self, input):
        env_1 = {"side1": 10, "side2": 10}
        env_2 = {"side1": 10, "side2": 10}
        expected = (env_1, env_2)
        result = Envelops.input_parameters()
        self.assertEqual(result, expected)

    def test_validate_side_valid_value(self):
        expected = 9.9
        result = Envelops.validate_side("9.9")
        self.assertEqual(result, expected)

    @patch("Envelops.input_text", return_value="15")
    def test_validate_side_text_value(self, input):
        expected = 15
        result = Envelops.validate_side("text")
        self.assertEqual(result, expected)

    @patch("Envelops.input_text", return_value="20")
    def test_validate_side_negative_value(self, input):
        expected = 20
        result = Envelops.validate_side("-7.7")
        self.assertEqual(result, expected)

    def test_is_sqrt_sides_greater_true_value(self):
        env_1 = {"side1": 3, "side2": 5}
        env_2 = {"side1": 2, "side2": 4}
        result = Envelops.is_sqrt_sides_greater(env_1, env_2)
        self.assertTrue(result)

    def test_is_sqrt_sides_greater_false_value(self):
        env_1 = {"side1": 2, "side2": 3}
        env_2 = {"side1": 4, "side2": 3}
        result = Envelops.is_sqrt_sides_greater(env_1, env_2)
        self.assertFalse(result)

    def test_is_sum_sides_bigger_true_value(self):
        env_1 = {"side1": 5, "side2": 3}
        env_2 = {"side1": 4, "side2": 3}
        result = Envelops.is_sum_sides_bigger(env_1, env_2)
        self.assertTrue(result)

    def test_is_sum_sides_bigger_false_value(self):
        env_1 = {"side1": 2, "side2": 3}
        env_2 = {"side1": 4, "side2": 3}
        result = Envelops.is_sum_sides_bigger(env_1, env_2)
        self.assertFalse(result)

    def test_is_min_sides_bigger_true_value(self):
        env_1 = {"side1": 5, "side2": 4}
        env_2 = {"side1": 4, "side2": 3}
        result = Envelops.is_min_side_bigger(env_1, env_2)
        self.assertTrue(result)

    def test_is_min_sides_bigger_false_value(self):
        env_1 = {"side1": 7, "side2": 3}
        env_2 = {"side1": 4, "side2": 3}
        result = Envelops.is_min_side_bigger(env_1, env_2)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()

import ChessBoard
import unittest


class TestChessBoard(unittest.TestCase):
    def test_valid_value(self):
        expected = "* * * * * \n * * * * *\n"
        result = ChessBoard.print_chess_board("10", "2")
        self.assertEqual(result, expected)

    def test_text_value(self):
        expected = "Wrong! It should be integer numbers."
        result = ChessBoard.print_chess_board("word", "input")
        self.assertEqual(result, expected)

    def test_negative_value(self):
        expected = "Chessboard sizes should be positive."
        result = ChessBoard.print_chess_board("7", "-10")
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

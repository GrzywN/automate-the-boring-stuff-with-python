import unittest


def is_valid_chess_board(chess_board) -> bool:
    figures_required = {
        "wpawn": 8,
        "wknight": 2,
        "wbishop": 2,
        "wrook": 2,
        "wqueen": 1,
        "wking": 1,
        "bpawn": 8,
        "bknight": 2,
        "bbishop": 2,
        "brook": 2,
        "bqueen": 1,
        "bking": 1
    }

    for field, figure in chess_board.items():
        if figure not in figures_required:
            return False

        figures_required[figure] -= 1

    for val in figures_required.values():
        if val != 0:
            return False

    return True


class TestChessBoardValidator(unittest.TestCase):

    def test_chess_board_on_valid_input(self):
        valid_chess_board = {
            "1a": "wrook", "1b": "wknight", "1c": "wbishop", "1d": "wqueen",
            "1e": "wking", "1f": "wbishop", "1g": "wknight", "1h": "wrook",
            "2a": "wpawn", "2b": "wpawn", "2c": "wpawn", "2d": "wpawn",
            "2e": "wpawn", "2f": "wpawn", "2g": "wpawn", "2h": "wpawn",
            "8a": "brook", "8b": "bknight", "8c": "bbishop", "8d": "bqueen",
            "8e": "bking", "8f": "bbishop", "8g": "bknight", "8h": "brook",
            "7a": "bpawn", "7b": "bpawn", "7c": "bpawn", "7d": "bpawn",
            "7e": "bpawn", "7f": "bpawn", "7g": "bpawn", "7h": "bpawn"}

        self.assertTrue(is_valid_chess_board(valid_chess_board))

    def test_chess_board_on_invalid_input(self):
        invalid_chess_board = {
            "1a": "wrook", "1b": "wknight", "1c": "wbishop", "1d": "wqueen",
            "1e": "wrook", "1f": "wbishop", "1g": "wknight", "1h": "wrook",
            "2a": "wpawn", "2b": "wpawn", "2c": "wpawn", "2d": "wpawn",
            "2e": "wpawn", "2f": "wpawn", "2g": "wpawn", "2h": "wpawn",
            "8a": "brook", "8b": "bknight", "8c": "bbishop", "8d": "bqueen",
            "8e": "bking", "8f": "bbishop", "8g": "bknight", "8h": "brook",
            "7a": "bpawn", "7b": "bpawn", "7c": "bpawn", "7d": "bpawn",
            "7e": "bpawn", "7f": "bpawn", "7g": "bpawn", "7h": "bpawn"}

        self.assertFalse(is_valid_chess_board(invalid_chess_board))


if __name__ == "__main__":
    unittest.main()

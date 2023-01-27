import unittest
from random import randint

TAILS = "r"
HEADS = "o"
HOW_MANY_CONSECUTIVE = 6


def simulate_coin_throws(n):
    throws = []
    for _ in range(n):
        throws.append(HEADS if randint(0, 1) == 0 else TAILS)

    return throws


def count_consecutive_coin_throws(throws):
    max_consecutive_coin_throws = 0
    curr_consecutive_coin_throws = 0
    last_throw = None

    for throw in throws:
        if last_throw is None:
            last_throw = throw
            curr_consecutive_coin_throws = 1
            continue

        if throw == HEADS and last_throw == HEADS:
            curr_consecutive_coin_throws += 1
        elif throw == TAILS and last_throw == TAILS:
            curr_consecutive_coin_throws += 1
        else:
            last_throw = throw
            curr_consecutive_coin_throws = 1

        max_consecutive_coin_throws = max(max_consecutive_coin_throws, curr_consecutive_coin_throws)

    return max_consecutive_coin_throws


class TestCoinFunctions(unittest.TestCase):

    def test_simulate_coin_throws(self):
        throws = simulate_coin_throws(10)

        contains_heads = HEADS in throws
        contains_tails = TAILS in throws
        contains_heads_or_tails = contains_heads or contains_tails

        self.assertTrue(contains_heads_or_tails)

    def test_count_consecutive_coin_throws(self):
        consecutive_coin_throws = count_consecutive_coin_throws([TAILS, TAILS, HEADS])

        self.assertEqual(consecutive_coin_throws, 2)

if __name__ == '__main__':
    number_of_streaks = 0

    for experiment_number in range(10000):
        throws = simulate_coin_throws(100)
        consecutive_coin_throws = count_consecutive_coin_throws(throws)
        if consecutive_coin_throws >= HOW_MANY_CONSECUTIVE:
            number_of_streaks += 1

    probability_of_consecutive = number_of_streaks / 100
    print(f"Prawdopodobieństwo wystąpienia serii: {probability_of_consecutive}")

    unittest.main()

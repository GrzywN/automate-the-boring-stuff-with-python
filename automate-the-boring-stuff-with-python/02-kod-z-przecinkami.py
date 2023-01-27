import unittest


def implode(words):
    return ", ".join(words[:-1]) + " i " + words[-1]


class TestImplode(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(implode(['jabłka', 'banany', 'tofu', 'koty']), 'jabłka, banany, tofu i koty')


if __name__ == '__main__':
    unittest.main()

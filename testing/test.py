import unittest
from testing.main import add_num


class TestMain(unittest.TestCase):
    def test_add_num(self):
        num = 10
        result = add_num(11)
        self.assertEqual(result, 16)


if __name__ == '__main__':
    unittest.main()

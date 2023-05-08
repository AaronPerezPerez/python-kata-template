import unittest

import fizzbuzz


class FizzBuzzTest(unittest.TestCase):
    def test_should_return_the_number_as_string(self):
        result = fizzbuzz.convert(1)
        self.assertEqual(result, "1")


if __name__ == '__main__':
    unittest.main()

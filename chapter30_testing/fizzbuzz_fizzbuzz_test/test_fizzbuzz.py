import fizzbuzz
import unittest

class TestFizzBuzz(unittest.TestCase):

    def test_multiple_of_three(self):
        self.assertEqual(fizzbuzz.process(6), 'Fizz')

    def test_multiple_of_five(self):
        self.assertEqual(fizzbuzz.process(20), 'Buzz')

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz.process(15), 'FizzBuzz')

if __name__ == '__main__':
    unittest.main()
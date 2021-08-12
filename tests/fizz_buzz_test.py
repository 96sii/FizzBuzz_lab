import unittest

from src.fizz_buzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
	def test_fizz_buzz_3(self):
		self.assertEqual("Fizz", fizz_buzz(3))

	def test_fizz_buzz_5(self):
		self.assertEqual("Buzz", fizz_buzz(5))

	def test_fizz_buzz_15(self):
		self.assertEqual("FizzBuzz", fizz_buzz(15))

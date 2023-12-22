from unittest import TestCase

from stage2 import extract_first_digit, extract_last_digit

class TestDay2(TestCase):
  def test0(self):
    s = 'two1nine'
    self.assertEqual('2', extract_first_digit(s))
    self.assertEqual('9', extract_last_digit(s))

  def test1(self):
    s = 'eightwothree'
    self.assertEqual('8', extract_first_digit(s))
    self.assertEqual('3', extract_last_digit(s))

  def test2(self):
    s = 'abcone2threexyz'
    self.assertEqual('1', extract_first_digit(s))
    self.assertEqual('3', extract_last_digit(s))

  def test3(self):
    s = 'xtwone3four'
    self.assertEqual('2', extract_first_digit(s))
    self.assertEqual('4', extract_last_digit(s))

  def test4(self):
    s = '4nineeightseven2'
    self.assertEqual('4', extract_first_digit(s))
    self.assertEqual('2', extract_last_digit(s))

  def test5(self):
    s = 'zoneight234'
    self.assertEqual('1', extract_first_digit(s))
    self.assertEqual('4', extract_last_digit(s))

  def test6(self):
    s = '7pqrstsixteen'
    self.assertEqual('7', extract_first_digit(s))
    self.assertEqual('6', extract_last_digit(s))



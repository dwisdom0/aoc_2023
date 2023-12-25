from unittest import TestCase

from stage2 import extract_gear_ratios


class Test2(TestCase):

  def test0(self):
    """
    the example from the prompt
    """
    schematic = [
      ['4', '6', '7', '.', '.', '1', '1', '4', '.', '.'],
      ['.', '.', '.', '*', '.', '.', '.', '.', '.', '.'],
      ['.', '.', '3', '5', '.', '.', '6', '3', '3', '.'],
      ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
      ['6', '1', '7', '*', '.', '.', '.', '.', '.', '.'],
      ['.', '.', '.', '.', '.', '+', '.', '5', '8', '.'],
      ['.', '.', '5', '9', '2', '.', '.', '.', '.', '.'],
      ['.', '.', '.', '.', '.', '.', '7', '5', '5', '.'],
      ['.', '.', '.', '$', '.', '*', '.', '.', '.', '.'],
      ['.', '6', '6', '4', '.', '5', '9', '8', '.', '.']
    ]

    ratios = extract_gear_ratios(schematic)
    self.assertEqual(467*35 + 755*598, sum(ratios))

  def test1(self):
    """
    yep this is the issue

    I found it in the data
    980....
    ...*980
    .......
    
    so I think I can get away with doing 1 set per line then
    instead of 1 set for all the neighbors
      
    """
    schematic = [
      ['3', '2', '1', '.'],
      ['3', '2', '1', '*'],
      ['3', '2', '1', '.'],
    ]
    ratios = extract_gear_ratios(schematic)
    self.assertEqual(321*321*321, sum(ratios))

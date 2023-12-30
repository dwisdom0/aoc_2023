from unittest import TestCase
from stage1 import Mapping, Map


class Test1(TestCase):
  def test_mapping0(self):
    m = Mapping(50, 98, 2)
    self.assertEqual(m.map(98), 50)
    self.assertEqual(m.map(99), 51)

  def test_mapping1(self):
    m = Mapping(52, 50, 48) 
    self.assertEqual(m.map(53), 55)
  
  def test_map(self):
    m = Map([50, 52], [98, 50], [2, 48])
    self.assertTrue(51 in m)
    self.assertFalse(49 in m)
    self.assertEqual(528, m.map(528))
    self.assertEqual(m.map(53), 55)
    self.assertEqual(m.map(99), 51)


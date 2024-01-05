from random import randint
from unittest import TestCase

from stage1 import predict


class Test1(TestCase):
  def setUp(self):
    print()

 
  def test1(self):
    history = [0, 3, 6, 9, 12, 15]
    self.assertEqual(18, predict(history))

  def test2(self):
    history = [1, 3, 6, 10, 15, 21]
    self.assertEqual(28, predict(history))

  def test3(self):
    history = [10, 13, 16, 21, 30, 45]
    self.assertEqual(68, predict(history))

  def test4(self):
    history = [-1, -3, -6, -10, -15, -21]
    self.assertEqual(-28, predict(history))

  def test5(self):
    history = [4, -1, -6, -11, -16, -21, -26, -31, -36, -41, -46, -51, -56, -61, -66, -71, -76, -81, -86, -91, -96]
    self.assertEqual(-101, predict(history))

  @staticmethod
  def gen_history():
    layer = [randint(-20, 20)] * randint(3, 10)
    history_seed = randint(-20, 20)
    for _ in range(randint(2, 8)):
      next_layer = [history_seed]
      for diff in layer:
        next_layer.append(next_layer[-1] + diff)
      layer = next_layer
    
    return layer

#   def test_stress(self):
#     history = self.gen_history()
#     answer = history.pop(-1)
#     max_iter = 10_000
#     i = 0
#     while answer == predict(history) and i < max_iter:
#       history = self.gen_history()
#       answer = history.pop(-1)
#       i += 1
#     breakpoint()

  def test6(self):
    history = [16, 32, 64, 128, 256, 512, 1000, 1864, 3280, 5440]
    self.assertEqual(8528, predict(history))
    

    
    

      

    
from collections import Counter
from dataclasses import dataclass
from enum import Enum

class HandType(Enum):
  HIGH = 1
  PAIR = 2
  TWOPAIR = 3
  THREE = 4
  FULLHOUSE = 5
  FOUR = 6
  FIVE = 7

CARD_RANKS = {
  '1': 1,  # probably isn't a 1 but it makes the numbers nicer
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9,
  'T': 10,
  'J': 11,
  'Q': 12,
  'K': 13,
  'A': 14
}

@dataclass
class Hand:
  cards: str
  bid: int
  hand_type: HandType

  def __gt__(self, other):
    """self > other"""
    if self.hand_type.value > other.hand_type.value:
      return True
    elif self.hand_type == other.hand_type:
      for self_c, other_c in zip(self.cards, other.cards):
        if CARD_RANKS[self_c] > CARD_RANKS[other_c]:
          return True
        elif CARD_RANKS[self_c] < CARD_RANKS[other_c]:
          return False

    return False

  def __lt__(self, other):
    """self < other"""
    if self.hand_type.value < other.hand_type.value:
      return True
    elif self.hand_type == other.hand_type:
      for self_c, other_c in zip(self.cards, other.cards):
        if CARD_RANKS[self_c] < CARD_RANKS[other_c]:
          return True
        elif CARD_RANKS[self_c] > CARD_RANKS[other_c]:
          return False

    return False




def read_input(fpath):
  with open(fpath, 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
  
  hands = []
  for line in lines:
    cards, bid = line.split()
    bid = int(bid)
    hand = Hand(cards, bid, parse_cards(cards))
    hands.append(hand)

  return hands


def parse_cards(cards):
  """
  Takes in the cards and returns their HandType
  """
  c = Counter(cards)
  counts = [v for _, v in c.items()]
  if 5 in counts:
    return HandType.FIVE
  elif 4 in counts:
    return HandType.FOUR
  elif 3 in counts and 2 in counts:
    return HandType.FULLHOUSE
  elif 3 in counts:
    return HandType.THREE
  elif len([count for count in counts if count == 2]) == 2:
    return HandType.TWOPAIR
  elif 2 in counts:
    return HandType.PAIR
  else:
    return HandType.HIGH






def main():
  hands = read_input('input.txt')
  hands = sorted(hands)
  total = 0
  for i, hand in enumerate(hands, start=1):
    total += i * hand.bid
  
  print(total)



if __name__ == '__main__':
  main()
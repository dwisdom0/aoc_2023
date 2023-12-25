
class Card:
  def __init__(self, winners, haves):
    self.winners = winners
    self.haves = winners
    self.overlap = winners.intersection(haves)
    self.count = 1
  
  def score(self):
    return len(self.overlap)
  
def read_input(fpath):
  with open(fpath, 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

  cards = []
  for line in lines:
    _, data = line.split(':')
    win_data, have_data = data.split('|')
    winners = win_data.split()
    winners = {w for w in winners}
    haves = have_data.split()
    haves = {h for h in haves}
    cards.append(Card(winners, haves))
  return cards


def main():
  cards = read_input('input.txt')
  for i, card in enumerate(cards):
    for j in range(i+1, i+card.score()+1):
      cards[j].count += 1 * card.count
  
  total = 0
  for card in cards:
    total += card.count
  
  print(total)




  


if __name__ == '__main__':
  main()

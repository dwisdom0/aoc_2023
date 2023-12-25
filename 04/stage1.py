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
    cards.append({
      'winners': winners,
      'haves': haves,
      'overlap': winners.intersection(haves)
    })
  return cards

def score(card):
  matches = len(card['overlap'])
  if matches == 0:
    return 0

  return 2 ** (matches - 1)

def main():
  cards = read_input('input.txt')
  print(sum([score(card) for card in cards]))


if __name__ == '__main__':
  main()

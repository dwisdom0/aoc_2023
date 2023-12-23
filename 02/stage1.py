def read_input(fpath):
  with open(fpath, 'r') as f:
    lines = f.readlines()
    return [l.strip() for l in lines]

def extract_game_data(line):
  game_id, turns = line.split(':')
  game_id = int(game_id.replace('Game ', ''))
  turns = turns.strip().split(';')
  
  max_r = 0
  max_g = 0
  max_b = 0
  for turn in turns:
    for pull in turn.strip().split(','):
      pull = pull.strip()
      count, color = pull.split(' ')
      color = color.strip()
      count = int(count)
      if color == 'red' and count > max_r:
        max_r = count
      elif color == 'green' and count > max_g:
        max_g = count
      elif color == 'blue' and count > max_b:
        max_b = count
      elif color not in {'red', 'green', 'blue'}:
        raise ValueError(f'color must be one of "red", "green", or "blue". Got {color}')
  
  return {'max_r': max_r, 'max_g': max_g, 'max_b': max_b}

def is_possible_game(game_max):
  max_r_allowed = 12
  max_g_allowed = 13
  max_b_allowed = 14
  for color, max_color_allowed in zip(['max_r', 'max_g', 'max_b'], [max_r_allowed, max_g_allowed, max_b_allowed]):
    if game_max[color] > max_color_allowed:
      return False
  return True


def main():
  lines = read_input("input.txt")
  game_maxes = [extract_game_data(line) for line in lines]
  possible_mask = [is_possible_game(game_max) for game_max in game_maxes]
  total = 0
  for i, possible in enumerate(possible_mask, start=1):
    if possible:
      total += i
  print(total)



if __name__ == '__main__':
  main()
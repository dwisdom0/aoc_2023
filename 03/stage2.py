from copy import deepcopy

def read_input(fpath):
  with open(fpath, 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
  schematic = []
  for line in lines:
    schematic.append([c for c in line])
  return schematic

def get_grid_value(grid, i, j):
  if i < 0 or j < 0:
    return '.'

  try:
    return grid[i][j]
  except IndexError:
    return '.'

def extract_number(schematic, i, j):
  # seach backward and forwards to find the limits of the number
  DIGITS = '1234567890'
  start_j = deepcopy(j)
  while get_grid_value(schematic, i, start_j-1) in DIGITS:
    start_j -= 1
  
  end_j = deepcopy(j)
  while get_grid_value(schematic, i, end_j+1) in DIGITS:
    end_j += 1
  
  number = schematic[i][start_j: end_j+1]
  return int(''.join(number))
  
def calculate_gear_ratio(schematic, i, j):
  start_r = i - 1
  end_r = i + 1
  start_c = j - 1
  end_c = j + 1

  DIGITS = '1234567890'
  # search for numbers in the the 3x3 box around the asterix
  # there's one place where we have two of the same number touching the gear
  # but they're on different rows
  # so we can do one set per row to dedupe
  numbers = []
  for r in range(start_r, end_r+1):
    row_set = set()
    for c in range(start_c, end_c+1):
      if get_grid_value(schematic, r, c) not in DIGITS:
        continue
      row_set.add(extract_number(schematic, r, c))
    numbers.extend(list(row_set))
  
  # If we don't have multiple numbers,
  # it's not a gear ratio
  if len(numbers) <= 1:
    return 0
  
  gear_ratio = 1
  for number in numbers:
    gear_ratio *= number
  
  return gear_ratio

def extract_gear_ratios(schematic):
  gear_ratios = []
  for i, row in enumerate(schematic):
    for j, val in enumerate(row):
      if val == '*':
        gear_ratios.append(calculate_gear_ratio(schematic, i, j))
  return gear_ratios



def main():
  schematic = read_input('input.txt')
  print(sum(extract_gear_ratios(schematic)))

  # 72114486
  # too low


if __name__ == '__main__':
  main()

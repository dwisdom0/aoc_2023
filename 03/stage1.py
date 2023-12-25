def read_input(fpath):
  with open(fpath, 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
  grid = []
  for line in lines:
    row = []
    for c in line:
      row.append(c)
    grid.append(row)

  return grid

def get_grid_value(grid, i, j):
  if i < 0 or j < 0:
    return '.'

  try:
    return grid[i][j]
  except IndexError:
    return '.'

def is_valid_number(grid, i, start_j, length):
  end_j = start_j + length - 1
  neighbors = []
  neighbors.append(get_grid_value(grid, i, start_j-1))
  neighbors.append(get_grid_value(grid, i, end_j+1))
  for j in range(start_j-1, end_j+1+1):
    neighbors.append(get_grid_value(grid, i-1, j))
    neighbors.append(get_grid_value(grid, i+1, j))
  
  # number = grid[i][start_j:end_j+1]
  # print(number)
  # print(neighbors)
  # breakpoint()

  for neighbor in neighbors:
    if neighbor in '1234567890':
      raise ValueError(f"Got a digit in the neighbors")
    elif neighbor != '.':
      return True

  return False

def extract_valid_numbers(schematic):
  DIGITS = '1234567890'
  valid_numbers = []
  for i, row in enumerate(schematic):
    j = 0
    while j < len(row):
      # print(f'{j=}')
      if row[j] in DIGITS:
        # find the end of the number
        num_len = 1
        if get_grid_value(schematic, i, j+1) not in DIGITS:
          num_len = 1
        elif get_grid_value(schematic, i, j+2) not in DIGITS:
          num_len = 2
        elif get_grid_value(schematic, i, j+3) not in DIGITS:
          num_len = 3

        if is_valid_number(schematic, i, j, num_len):
          # using the unsafe access instead of my function
          # since we know the indexes will be fine
          # and I need a slice
          valid_numbers.append(int(''.join(schematic[i][j:j+num_len])))
        
        # set j to the end of the number
        j += num_len
        continue
      
      # if we didn't find a number, increment j
      j += 1

  
  return valid_numbers



def main():
  schematic = read_input('input.txt')
  print(sum(extract_valid_numbers(schematic)))
  # 499822
  # too low






if __name__ == '__main__':
  main()
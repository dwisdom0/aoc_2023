def read_input(fpath):
  with open(fpath, 'r') as f:
    lines = f.readlines()

  # split into individual characters
  lines = [[c for c in line.strip()] for line in lines]

  # save the starting point and replace it with the proper character
  for i, row in enumerate(lines):
    for j, val in enumerate(row):
      if val == 'S':
        start = (i, j)
        # I happen to know it's supposed to be this character
        # because I looked at the input
        lines[i][j] = '-'

  # replace all the maze characters with Node objects
  maze = []
  for i, row in enumerate(lines):
    new_row = []
    for j, val in enumerate(row):
      new_row.append(Node(i, j, val)) 
    maze.append(new_row)


  return start, maze


class Node:
  def __init__(self, i, j, pipe_char):
    self.i = i
    self.j = j
    self.pipe_char = pipe_char

    if pipe_char == '.':
      self.neighbors = None
      return
    elif pipe_char == '|':
      self.neighbors = (
        self.north(),
        self.south()
      )
    elif pipe_char == '-':
      self.neighbors = (
        self.west(),
        self.east()
      )
    elif pipe_char == 'L':
      self.neighbors = (
        self.north(),
        self.east()
      )
    elif pipe_char == 'J':
      self.neighbors = (
        self.north(),
        self.west()
      )
    elif pipe_char == '7':
      self.neighbors = (
        self.south(),
        self.west()
      )
    elif pipe_char == 'F':
      self.neighbors = (
        self.south(),
        self.east()
      )
    else:
      raise ValueError(f"unrecognized pipe char {pipe_char}")

  @staticmethod
  def edgesafe(val):
    if val < 0 or val > 139:
      return None
    return val

  def north(self):
    return (self.edgesafe(self.i-1), self.j)

  def south(self):
    return (self.edgesafe(self.i+1), self.j)

  def east(self):
    return (self.i, self.edgesafe(self.j+1))

  def west(self):
    return (self.i, self.edgesafe(self.j-1))

  def __repr__(self):
    return f"Node({self.i}, {self.j}, {self.pipe_char}), neighbors {self.neighbors}"


def main():
  start, maze = read_input('input.txt')
  prev_idx = start
  cur_node = maze[start[0]][start[1]+1]
  steps = 1
  visited_idxs = []
  while prev_idx != (start[0], start[1]-1):
    next_idx = cur_node.neighbors[0]
    if next_idx == prev_idx:
      next_idx = cur_node.neighbors[1]
    visited_idxs.append(next_idx)
    prev_idx = (cur_node.i, cur_node.j)
    cur_node = maze[next_idx[0]][next_idx[1]]
    steps += 1

#   print(visited_idxs)
  print(steps)
  print(steps // 2)



if __name__ == '__main__':
  main()


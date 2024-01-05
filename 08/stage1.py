class Node:
  def __init__(self, n, l, r):
    self.n = n
    self.l = l
    self.r = r


def read_input(fpath):
  with open(fpath, 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

  directions = lines.pop(0)

  # pop the empty line
  lines.pop(0)

  network = {}
  for line in lines:
    line = line.replace('(', '').replace(')', '')
    n, lr = line.split(' = ')
    l, r = lr.split(', ')
    network[n] = Node(n, l, r)

  return directions, network


def main():
  directions, network = read_input('input.txt')
  cur_node= 'AAA'
  i = 0
  while cur_node != 'ZZZ':
    direction = directions[i % len(directions)]

    node = network[cur_node]

    if direction == 'L':
      cur_node = node.l
    elif direction == 'R':
      cur_node = node.r
    
    i += 1

  print(i)
    



if __name__ == '__main__':
  main()



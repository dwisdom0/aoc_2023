from tqdm import tqdm
from functools import cache

def read_input(fpath):
  with open(fpath, 'r') as f:
    lines = f.readlines()
  lines = tuple([tuple([c for c in l.strip()]) for l in lines])

  return lines


@cache
def get_doubled_rows(universe):
  doubled_rows = set()
  for i, row in enumerate(universe):
    if '#' not in row:
      doubled_rows.add(i)
  return doubled_rows

@cache
def get_doubled_cols(universe):
  doubled_cols = set()
  for j in range(len(universe[0])):
    col = [universe[i][j] for i in range(len(universe))]
    if '#' not in col:
      doubled_cols.add(j)
  return doubled_cols

def dist(universe, i1, j1, i2, j2):
  big_i = max(i1, i2)
  small_i = min(i1, i2)
  big_j = max(j1, j2)
  small_j = min(j1, j2)

  distance = (big_i - small_i) + (big_j - small_j)
  for row in get_doubled_rows(universe):
    if small_i < row and row < big_i:
      distance += 1_000_000 - 1
  for col in get_doubled_cols(universe):
    if small_j < col < big_j:
      distance += 1_000_000 - 1

  return distance



def main():
  universe = read_input('input.txt')
  galaxies = []
  for i, row in enumerate(universe):
    for j, val in enumerate(row):
      if val == '#':
        galaxies.append((i, j))

  # compute pairwise distances for galaxies
  pairwise_dists = []
  for i, galaxy1 in tqdm(enumerate(galaxies), ascii=True, total=len(galaxies)):
    if i == len(galaxies) - 1:
      break
    for galaxy2 in galaxies[i+1:]:
      pairwise_dists.append(dist(universe, *galaxy1, *galaxy2))


  print(sum(pairwise_dists))
  
  # 513172286518
  # too high

if __name__ == '__main__':
  main()
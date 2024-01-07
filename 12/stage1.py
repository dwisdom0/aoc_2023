import math

from itertools import permutations

from tqdm import tqdm

def read_input(fpath):
  with open(fpath, 'r') as f:
    lines = f.readlines()
  lines = [l.strip() for l in lines]

  rows = []
  markers = []
  for line in lines:
    row, marker = line.split()
    rows.append([c for c in row])
    markers.append([int(m) for m in marker.split(',')])
  
  return rows, markers


def check(row, markers):
  start_idxs = []
  end_idxs = []
  in_run = False
  for i, val in enumerate(row):
    if val == '#' and not in_run:
      in_run = True
      start_idxs.append(i)
    elif val == '.' and in_run:
      in_run = False
      end_idxs.append(i)

  if len(start_idxs) != len(end_idxs):
    end_idxs.append(len(row))

  runs = []
  for start, end in zip(start_idxs, end_idxs):
    runs.append(end-start)

#   print(f'{runs=}')

  if runs == markers:
    return True
  return False


def try_all_possible(row, markers):
  replacement_idxs = []
  existing_hash_count = 0
  for i, c in enumerate(row):
    if c == '?':
      replacement_idxs.append(i)
    elif c == '#':
      existing_hash_count += 1
  num_hashes = sum(markers) - existing_hash_count
  replacements = (['#'] * num_hashes) + (['.'] * (len(replacement_idxs) - num_hashes))
  rows_already = set()
  hits = 0

  for perm in tqdm(permutations(replacement_idxs), ascii=True, total=math.factorial(len(replacement_idxs))):
    for j, idx in enumerate(perm):
      row[idx] = replacements[j]

    if tuple(row) in rows_already:
      continue

    if check(row, markers):
      print(row, markers)
      hits += 1

    rows_already.add(tuple(row))
  return hits





  


def main():
  rows, markers = read_input('input.txt')
  total = 0
  for row, marker in tqdm(zip(rows, markers), ascii=True, total=len(rows)):
    total += try_all_possible(row, marker)
    print()
    print(total)
    print()

  print(total)

  # still looking at 100k hours for 17 ?'s
  # ouch
  #
  # I don't really want to figure out something clever
  # think I'm gonna call it there

  



if __name__ == '__main__':
  main()
    
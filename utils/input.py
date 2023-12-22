def read_input(fpath):
  with open(fpath, 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
  return lines
    
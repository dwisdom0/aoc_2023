from tqdm import tqdm

def read_input(fpath):
  with open(fpath, 'r') as f:
    lines = f.readlines()
    lines = [l.strip().replace(' ','') for l in lines]

  time = lines.pop(0).split(':')
  time = int(time[1])

  record = lines.pop(0).split(':')
  record = int(record[1])

  return time, record

def distance(max_t, held_t):
  t = max_t - held_t
  v = held_t
  return v * t


def main():
  time, record = read_input('input.txt')

  # you're probably supposed to solve for the min and max
  # but it only takes a few seconds to brute force it
  win_count = 0
  for t in tqdm(range(time+1), ascii=True):
    if distance(time, t) > record:
      win_count += 1
  
  print(win_count)

if __name__ == '__main__':
  main()


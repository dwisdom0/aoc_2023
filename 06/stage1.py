

def read_input(fpath):
  with open(fpath, 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

  times = lines.pop(0).split()
  times = [int(t) for t in times[1:]]

  records = lines.pop(0).split()
  records = [int(r) for r in records[1:]]

  return times, records

def distance(max_t, held_t):
  t = max_t - held_t
  v = held_t
  return v * t


def main():
  times, records = read_input('input.txt')


  total = 1
  for max_time, record in zip(times, records):
    win_count = 0
    for t in range(max_time+1):
      if distance(max_time, t) > record:
        win_count += 1
    total *= win_count
  
  print(total)

if __name__ == '__main__':
  main()


from time import time

from tqdm import tqdm

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
    network[n] = {'L': l, 'R': r}

  return directions, network


def count_Z(nodes):
  total = 0
  for n in nodes:
    if n[-1] == 'Z':
      total += 1
  return total

def main():
  directions, network = read_input('input.txt')
  cur_nodes = tuple([k for k in network.keys() if k.endswith('A')])
  i = 0
  # if we have any nodes that don't end with Z, loop again
  start = time()
  max_endpoints = 0
  max_iter = 1_000_000_000
  # progress bar
  t = tqdm(total=max_iter, ascii=True)
  while count_Z(cur_nodes) != len(cur_nodes) and i < max_iter:
    t.update(1)

    # debugging progress print out
    # num_endpoints = count_Z(cur_nodes)
    # if num_endpoints > max_endpoints:
    #   print(f'new max: {i} {num_endpoints}')
    #   max_endpoints = deepcopy(num_endpoints)

    direction = directions[i % len(directions)]

    new_cur_nodes = []
    for cur_node in cur_nodes:
      new_cur_nodes.append(network[cur_node][direction])

    cur_nodes = tuple(new_cur_nodes)
    
    i += 1
  t.close()

  print(i)
  # print(f'{max_endpoints=}')
  # print(f'{max_endpoints_nodes=}')
  print(f'took {time() - start:.2f} seconds')
    



if __name__ == '__main__':
  main()

  # new max: 13019 1 ['LQZ']
  # new max: 690007 2 ['LQZ', 'FQZ']
  # new max: 40710413 3 ['LQZ', 'ZZZ', 'FQZ']
  # 1000000000
  # max_endpoints=3
  # max_endpoints_nodes=['LQZ', 'ZZZ', 'FQZ']
  # took 5047.96 seconds

  # so going for 1 trillion iterations didn't find anything above 3
  # found 3 at only 40 million iterations
  # I need 6

  # options
  # 1. profile with scalene and try to improve search speed
  #    - cache stuff? it's already just a dict lookup so it's basically cached already
  #    - actually build the network instead of doing a dict of nodes? then I could go from 2 dict lookups to 1 probably
  #    - don't do that until the profiler says to though
  #    - 50% of the time is spent calling deepcopy(new_cur_nodes)
  #    - 25% is the list comprenhension + .endswith() to check for Z nodes each loop
  #    - 17% for new_current_nodes.append()
  #    - 11% for a second list comprehension + endswith() for the debugging printouts
  #    - everything else is literally 0 unmeasureable
  #    - yeah so not much to optimize there
  #    - I guess I could cache the list comprehension + .endswith() check
  #        - doing that with a counter and a loop actually turned out to be faster than caching it
  #        - even when I had did it twice every loop for debugging print outs
  #    - got it down from 84 minutes to 22 minutes for 1 trillion iterations
  #    - I think there must be something I'm missing
  #    - some clever way of solving it that isn't just implementing the algorithm they describe
  # 2. try to start at the end and go backwards? 
  #    - I don't really know how that would help
  # 3. debug very carefully to make sure I'm actually doing exactly the right thing each step
  #    - something about the modulo for the repeating directions? but it worked fine for stage 1
  #    - test cases I guess
  #




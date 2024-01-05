from copy import deepcopy

from tqdm import tqdm

def read_input(fpath):
  with open(fpath, 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

  histories = []
  for line in lines:
    histories.append([int(reading) for reading in line.split()])

  return histories

def diffs(history):
  diffs = []
  for i in range(1, len(history)):
    diffs.append(history[i] - history[i-1])
  return diffs

def predict(history):
  print(history)
  layer = deepcopy(history)
  d = diffs(layer)
  
  # base case: we've got all 0s in the diff layer
  if sum(d) == 0 and len(set(d)) == 1:
    return layer[-1]

  # recursive case: we need to go down another layer
  # because we don't have all 0s yet
  deeper_layer_val = predict(d)

  # base case: we're on the way back up so we need to return this layer's next value
  to_return = deeper_layer_val + layer[-1]
  print(layer + [to_return])
  return to_return


  


def main():
  histories = read_input('input.txt')

  results = []
  for history in tqdm(histories, ascii=True):
    print()
    print(history)
    result = predict(history)
    results.append(result)
    print(result)
    print()

  print(len(histories))
  print(len(results))
  print(sum(results))

  # 1995001998
  # too high

  # I have no idea what's wrong
  # I tried to make some test cases but everything passes
  # manually worked through a few and they match as well
  # double-checked that I'm using exactly the right input
  # I don't really know where to go from here

  # okay finally found a bugged test case
  # 
  # (Pdb) history
  # [16, 32, 64, 128, 256, 512, 1000, 1864, 3280, 5440]
  # (Pdb) answer
  # 8528
  # (Pdb) predict(history)
  # [16, 32, 64, 128, 256, 512, 1000, 1864, 3280, 5440]
  # [16, 32, 64, 128, 256, 488, 864, 1416, 2160]
  # [16, 32, 64, 128, 232, 376, 552, 744]
  # [16, 32, 64, 104, 144, 176, 192]
  # [16, 32, 40, 40, 32, 16]
  # [16, 32, 64, 104, 144, 176, 192, 208]
  # [16, 32, 64, 128, 232, 376, 552, 744, 952]
  # [16, 32, 64, 128, 256, 488, 864, 1416, 2160, 3112]
  # [16, 32, 64, 128, 256, 512, 1000, 1864, 3280, 5440, 8552]
  # 8552
  #
  # oh duh because I'm checking if the sum is 0
  # but you can have 2 non-zero things add up to 0
  # jeez


if __name__ == '__main__':
  main()
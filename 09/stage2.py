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
    return layer[0]

  # recursive case: we need to go down another layer
  # because we don't have all 0s yet
  deeper_layer_val = predict(d)

  # base case: we're on the way back up so we need to return this layer's next value
  to_return = layer[0] - deeper_layer_val
  print([to_return] + layer)
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


if __name__ == '__main__':
  main()
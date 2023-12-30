from copy import deepcopy

from tqdm import tqdm

class Range:
  def __init__(self, start, extent):
    self.start = start
    self.end = start + extent - 1

    # might not need this one
    self.extent = extent
  
  def __contains__(self, item):
    if item >= self.start and item <= self.end:
      return True
    return False

  def __repr__(self):
    return f"{self.start} - {self.end}"

class Mapping:
  def __init__(self, dst_start, src_start, extent):
    self.dst = Range(dst_start, extent)
    self.src = Range(src_start, extent)
  
  def map(self, val):
    if val not in self.src:
      raise ValueError(f"value {val} not in {self.src}")
    
    return self.dst.start + val - self.src.start
  
  def __contains__(self, item):
    return item in self.src


class Map:
  def __init__(self, dsts, srcs, extents):
    self.mappings = []
    for dst, src, extent in zip(dsts, srcs, extents):
      self.mappings.append(Mapping(dst, src, extent))
  
  def map(self, val):
    """
    take a source value and map it to a destination value

    if the value isn't in any maps, we return the value as-is
    """
    for mapping in self.mappings:
      if val in mapping:
        return mapping.map(val)
    return val
  
  def __contains__(self, item):
    for mapping in self.mappings:
      if item in mapping.src:
        return True
    return False


def map_seeds(seeds, maps):
  locations = []
  for seed in tqdm(seeds, ascii=True):
    new_val = deepcopy(seed)
    for map in maps:
      new_val = map.map(new_val)
    locations.append(new_val)
  return locations


def extract_next_map(lines):
  line = lines.pop(0)
  dsts = []
  srcs = []
  extents = []
  while not line.endswith(" map:"):
    if line == '':
      line = lines.pop(0)
      continue

    dst, src, extent = line.split()
    dsts.append(int(dst))
    srcs.append(int(src))
    extents.append(int(extent))
    try:
      line = lines.pop(0)
    except IndexError:
      break
  return Map(dsts, srcs, extents)


def read_input(fpath):
  with open(fpath, 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
  
  seeds = lines.pop(0)
  seeds = [int(seed) for seed in seeds.split()[1:]]

  # drop the blank line and the section title
  lines.pop(0)
  lines.pop(0)

  # seed to soil map
  print('extracting seed2soil')
  seed2soil = extract_next_map(lines)
  print('done')
  
  # soil to fertilizer map
  print('extracting soil2fert')
  soil2fert = extract_next_map(lines)
  print('done')

  # fertilizer to water map
  fert2water = extract_next_map(lines)

  # water to light map
  water2light = extract_next_map(lines)

  # light to temperature map
  light2temp = extract_next_map(lines)

  # temp to humidity map
  temp2humid = extract_next_map(lines)

  # humidity to location map
  humid2loc = extract_next_map(lines)

  all_maps = [
    seed2soil,
    soil2fert,
    fert2water,
    water2light,
    light2temp,
    temp2humid,
    humid2loc
  ]

  return seeds, all_maps



def main():
  seeds, all_maps = read_input('input.txt')
  locations = map_seeds(seeds, all_maps)

  print(min(locations))




if __name__ == '__main__':
  main()


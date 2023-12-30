# this solution takes 20 hours single-threaded on my laptop
# 
# obviously not the correct solution
#
# I think you can probably do something clever by starting at the locations
# and running it backwards.
# like start at location 0 and then go up until you get a hit
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
  
  def __iter__(self):
    for val in range(self.start, self.end+1):
      yield val
  
  def __repr__(self):
    return f"{self.start} - {self.end}"
  
  def __len__(self):
    return self.end - self.start + 1

class Mapping:
  def __init__(self, dst_start, src_start, extent):
    self.dst = Range(dst_start, extent)
    self.src = Range(src_start, extent)
  
  def map(self, val):
    if val not in self.src:
      raise ValueError(f"value {val} not in {self.src}")
    
    return self.dst.start + val - self.src.start
  
  def inverse_map(self, val):
    if val not in self.dst:
      raise ValueError(f"value {val} not in {self.dst}")

    return self.src.start + val - self.dst.start
    

  
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
  
  def inverse_map(self, val):
    for mapping in self.mappings:
      if val in mapping.dst:
        return mapping.inverse_map(val)
    return val

  
  def __contains__(self, item):
    for mapping in self.mappings:
      if item in mapping.src:
        return True
    return False


def apply_all_maps_inverse(val, maps):
  new_val = deepcopy(val)
  for map in maps:
    new_val = map.inverse_map(new_val)
  return new_val


def extract_next_map(lines):
  line = lines.pop(0)
  data = []
  while not line.endswith(" map:"):
    if line == '':
      line = lines.pop(0)
      continue

    data.append([int(x) for x in line.split()])

    try:
      line = lines.pop(0)
    except IndexError:
      break
  
  # sort by dst
  data = sorted(data, key=lambda x: x[0])

  dsts = [x[0] for x in data]
  srcs = [x[1] for x in data]
  extents = [x[2] for x in data]


  return Map(dsts, srcs, extents)


def read_input(fpath):
  with open(fpath, 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
  
  seeds = lines.pop(0)
  seeds = [int(seed) for seed in seeds.split()[1:]]

  # have to group the seeds into batches of 2
  grouped_seeds = []
  for i in range(0, len(seeds), 2):
    grouped_seeds.append([seeds[i], seeds[i+1]])

  seed_ranges = []
  for group in grouped_seeds:
    seed_ranges.append(Range(group[0], group[1]))
  
  # drop the blank line and the section title
  lines.pop(0)
  lines.pop(0)

  # seed to soil map
  seed2soil = extract_next_map(lines)
  
  # soil to fertilizer map
  soil2fert = extract_next_map(lines)

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
  
  # we're going to do it backwards
  # so we'll apply the maps in reverse order
  all_maps.reverse()

  return seed_ranges, all_maps



def main():
  seed_ranges, all_maps = read_input('input.txt')
  locations = all_maps[0]

  found = False
  for location_mapping in locations.mappings:
    print(f'checking {location_mapping.dst}')
    for location in tqdm(location_mapping.dst, ascii=True):
      val = apply_all_maps_inverse(location, all_maps)
      for seed_range in seed_ranges:
        if val in seed_range:
          print()
          print(location)
          print()
          found = True
          break
      if found:
        break
    if found:
      break





if __name__ == '__main__':
  main()

  # 1474667130
  # too high

  # 1998211432
  # too high

  


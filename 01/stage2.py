DIGITS = '0123456789'
NAME2DIGIT = {
'zero': '0',
'one': '1',
'two': '2',
'three': '3',
'four': '4',
'five': '5',
'six': '6',
'seven': '7',
'eight': '8',
'nine': '9',
}

def read_input(fpath):
  with open(fpath, 'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
  return lines

def extract_first_digit(line):
  for i, c in enumerate(line):
    if c in DIGITS:
      return c
    for name in NAME2DIGIT.keys():
      try:
        if line[i:i+len(name)] == name:
          return NAME2DIGIT[name]
      except IndexError:
        pass

def extract_last_digit(line):
  line_r = ''.join(reversed(line))
  for i, c in enumerate(line_r):
    if c in DIGITS:
      return c
    for name in NAME2DIGIT.keys():
      candidate = ''.join(reversed(line_r[i:i+len(name)]))
      try:
        if candidate == name:
          return NAME2DIGIT[name]
      except IndexError:
        pass

def main():
  lines = read_input('input.txt')
  calibration_numbers = []


  for line in lines:
    first_digit = extract_first_digit(line)
    last_digit = extract_last_digit(line)
    calibration_numbers.append(int(first_digit + last_digit))

  print(sum(calibration_numbers))

if __name__ == "__main__":
  main()

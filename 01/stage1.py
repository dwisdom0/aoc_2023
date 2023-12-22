
def read_input(fpath):
  with open(fpath, 'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
  return lines

def main():
  lines = read_input('input.txt')
  print(lines[:5])
  DIGITS = '0123456789'
  calibration_numbers = []
  for line in lines:
    line_numbers = ''
    for c in line:
      if c in DIGITS:
        line_numbers += c
        break
    for c in line[::-1]:
      if c in DIGITS:
        line_numbers += c
        break
    calibration_numbers.append(int(line_numbers))

  print(sum(calibration_numbers))




if __name__ == "__main__":
  main()

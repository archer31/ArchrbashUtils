import argparse

def values_and_ranges(arg):
  value = []
  arg = arg.split(',')
  for part in arg:
    if '-' in part:
      part = part.split('-')
      value += range(int(part[0]), int(part[1]) + 1)
    else:
      value.append(int(part))
  return value


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('filename', type=argparse.FileType('r'),
                      help='filename to cat')
  parser.add_argument('lines', type=values_and_ranges,
                      help='the lines to print')
  args = parser.parse_args()
  for i, line in enumerate(args.filename.readlines()):
    if i+1 in args.lines:
      print(line, end='')

import argparse

def main():
  parser = argparse.ArgumentParser(description='prints out line numbers of lines with '
                                               'more than thresh characters')
  parser.add_argument('filenames', type=argparse.FileType('r'), nargs='+',
                      help='filename to check')
  parser.add_argument('thresh', type=int, default=0,
                      help='number of characters to print a line')
  args=parser.parse_args()
  for f in args.filenames:
    for i, line in enumerate(f):
      if args.thresh <= len(line):
        print(f'{f.name}:{i+1}:line {len(line)}')

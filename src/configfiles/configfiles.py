import argparse
import json
import os

json_file = 'configfiles.json'

data_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), json_file)

data = json.load(open(data_file_path))

parser = argparse.ArgumentParser()
parser.add_argument('type', help='the type of config file to generate',
                    type=str, choices=list(data), nargs='+',
                    metavar='type')

args = parser.parse_args()

def main():
  for file_type in args.type:
    file_path = os.path.join(os.environ['HOME'], *data[file_type]['dest'].split('/')[1:])
    if os.path.exists(file_path):
      exit(1)
    open(file_path, 'w').write(data[file_type]['content'])

if __name__ == '__main__':
  main()
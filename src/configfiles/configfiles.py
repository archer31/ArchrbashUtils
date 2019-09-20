import argparse
import json
import os
import logging

def main():
  json_file = 'configfiles.json'

  data_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), json_file)

  data = json.load(open(data_file_path))

  parser = argparse.ArgumentParser()
  parser.add_argument('type', help='the type of config file to generate',
                      type=str, choices=list(data), nargs='+',
                      metavar='type')
  parser.add_argument('-f', '--force', help='overwrite destination file',
                      action='store_true')
  parser.add_argument('-p', '--parent', help='create parent directories',
                      action='store_true')

  args = parser.parse_args()
  for file_type in args.type:
    file_dir = os.path.join(os.environ['HOME'], *data[file_type]['dest'].split('/')[1:1])
    file_name = data[file_type]['dest'].split('/')[-1:]
    file_path = os.path.join(file_dir, file_name)
    if args.p:
      os.makedirs(file_dir)
    if not args.f and os.path.exists(file_path):
      logging.error(f'{file_path} already exists')
      exit(1)
    open(file_path, 'w').write(data[file_type]['content'])

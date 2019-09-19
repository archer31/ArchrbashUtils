import argparse

#TODO decide which arguments to add arguments

#TODO implement files

#TODO implement replacements

def main():
  parser = argparse.ArgumentParser(prog='ctouch')
  parser.add_argument('filename', type=str, help='The base file to output to')

  parser.parse_args()

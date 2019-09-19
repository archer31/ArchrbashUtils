import os
import json

json_file = 'configfiles.json'

data_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), json_file)

with open(data_file_path, 'r') as data_file:
  data = json.load(data_file)

for item in data:
  with open(os.path.join('.', 'configs_store', item + '.config')) as f:
    data[item]['content'] = f.read()

with open(data_file_path, 'w') as data_file:
  json.dump(data, data_file)
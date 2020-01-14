#By Alina Clough and Ahmed Ragab
#read, print to terminal, save output to file

import csv
import json

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    rows = [dict(row) for row in rows] # Convert OrderedDict to regular dict

print(rows)


with open('vegetables.json', 'w') as f:
    json.dump(rows, f, indent=4)
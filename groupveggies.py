#Ahmed Ragab and Alina Clough
# Read vegtables.csv into a variable called vegtables.
import csv
import json
from pprint import pprint

with open('vegetables.csv', "r") as f:
	reader= csv.DictReader(f)
	rows=list(reader)
	vegetables=[dict(row) for row in rows]


# Group vegtables by color as a variable vegtables_by_color.
vegtables_by_color={}
for veggie in vegetables:
	color  = veggie["color"]
	if color in vegtables_by_color: 
		vegtables_by_color[color].append(veggie)
		pprint(vegtables_by_color)
	else: 
		vegtables_by_color[color]=[veggie]

		pprint(vegtables_by_color) 
		print("=================================")
		
# Output vegtables_by_color into a json called vegtables_by_color.json.
with open("vegtables_by_color.json","w") as f:
	json.dump(rows, f, indent=2)

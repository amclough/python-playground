#Read vegetables.csv into a variable called vegetables.
import csv
import json

with open('vegetables.csv', "r") as f:
	reader= csv.DictReader(f)
	rows=list(reader)
	vegetables=[dict(row) for row in rows]

print(vegetables)	
#Loop through vegetables and filter down to only green vegtables using a whitelist.
greenveggies = []
whitelist = ["green"]
for veggie in vegetables:
    if veggie['color'] in whitelist:
        greenveggies.append(veggie)

#Print veggies to the terminal
print(greenveggies)

#Write the veggies to a json file called greenveggies.json
with open("greenveggies.json","w") as f:
	json.dump(rows, f)

#Bonus: Output another csv called green_vegetables.csv
with open("green_vegetables.csv", "w") as f:
	writer=csv.writer(f)
	writer.writerow(["name","color"])
	for veggie in vegetables:
		if veggie['color'] in whitelist:
			writer.writerow([veggie["name"],veggie["color"]])


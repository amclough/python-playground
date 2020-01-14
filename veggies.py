#Alina Clough and Ahmed Ragab

import csv
vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]
#Write a python program that

#Loops through each vegetable

#In the loop, write the name of 
#each vegetable and the color into
# a CSV called vegetables.csv

with open('vegetables.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'color'])

	for veg in vegetables:
		veg_name = veg["name"]
		veg_color = veg["color"]
		row = [veg_name, veg_color]
		writer.writerow(row)



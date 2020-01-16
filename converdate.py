#Ahmed Ragab and Alina Clough
# Try it exercise on Python Date-Time

#Import functionality
from datetime import datetime

 #Set a variable birthday = "1-May-12".
birthday = "1-May-12"

 #Parse the date using datetime.datetime.strptime.

python_date = datetime.strptime(birthday, "%d-%B-%y")

# Use strftime to output a date that looks like "5/1/2012".
new_date = python_date.strftime("%-m/%-d/%Y") 

print(new_date)

#Bonus: Trying with a function

def convertdate(date):
	parsed_date = datetime.strptime(date,"%d-%B-%y")
	date_str = parsed_date.strftime("%-m/%-d/%Y") # 01/11/17
	return date_str

formatted_birthday=convertdate(birthday)
print(formatted_birthday)



# Write a Python program to write a Python dictionary to a csv file.
# After writing the CSV file read the CSV file and display the content.

import csv

# Data to be inserted

data = [{'Name': 'Keerthi', 'Age': 21, 'Country': 'United States'},
 {'Name': 'Amal Thomson', 'Age': 26, 'Country': 'Canada'},
 {'Name': 'Sara', 'Age': 20, 'Country': 'Switzerland'},
 {'Name': 'Rahul', 'Age': 23, 'Country': 'USA'},
 {'Name': 'Sreerag', 'Age': 24, 'Country': 'Neitherland'},
 {'Name': 'Sarath', 'Age': 23, 'Country': 'Ireland'},
 {'Name': 'John', 'Age': 20, 'Country': 'India'},
 {'Name': 'Subin', 'Age': 24, 'Country': 'New Zealand'},
 {'Name': 'Kavya', 'Age': 25, 'Country': 'Austarlia'}]

# Write to CSV file

with open('people.csv', 'w') as csvfile:
 headernames = ['Name', 'Age', 'Country']
 csvwriter = csv.DictWriter(csvfile, fieldnames=headernames)
 csvwriter.writeheader()
 for row in data:
  csvwriter.writerow(row)

# Read from CSV file and print contents

with open('people.csv', 'r') as csvfile:
 reader = csv.DictReader(csvfile)
 for row in reader:
  print(row)
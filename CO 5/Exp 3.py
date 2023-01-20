# Program to read each row from a given csv file and print a list of strings.

import csv

# Open the csv file
with open('names.csv','r') as file:
    # Create a csv reader
    reader = csv.reader(file)

 # Iterate over the rows of the CSV file
    for row in reader:
    # Print the rows as a list of strings
     print(row)
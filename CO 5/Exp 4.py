# Program to read specific columns of a given CSV file and print the content of the columns.

import csv

# specify the column indices that you want to read
# e.g. column 0 is the first column, column 1 is the second column, etc.
columns_to_read = [0,2]

# Open the CSV file and read the contents
with open('names.csv','r') as f:
    clmn_reader = csv.reader(f)

# Iterate over the rows of the CSV file
    for row in clmn_reader:
    # Print the rows as a list of strings
     print([row[i] for i in columns_to_read])
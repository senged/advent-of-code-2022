




import csv
import os
import pandas as pd
import numpy as np


# Function to read lines of a file
def read_lines(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line)
        return lines






# --------------

# Read a text file's last line and determine the row position for each element space-delimited
def read_last_line(file_name):
    with open(file_name, 'r') as f:
        last_line = f.readlines()[-1]
        #last_line = last_line.split()
        return last_line


# Split string characters into a list
def extract_chars(myString):
  newList = []
  for i in range(len(myString)):
    if myString[i] != ' ':
      newList.append([i,myString[i]])
  return newList


# ========================================
fp = os.path.join("day-5", "example-initial-stacks.csv")

lastLine = read_last_line(fp)
chars = extract_chars(lastLine)

# Parse string into characters
chars2 = list(lastLine)
print(chars2)




read_lines(fp)


print(lastLine)

# Read the CSV file into a DataFrame

df = pd.read_csv(fp, sep=' ', header=None)

# Convert the DataFrame to a NumPy array and transpose it
array = df.to_numpy().T

# Extract each column into a Python list
columns = [list(row) for row in array]

print(columns)
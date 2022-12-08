
import csv
import os
import pandas as pd
import numpy as np


# Function to read lines of a file
def readSteps(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        steps = []
        for line in lines:
          parts = line.split()
          if len(parts) == 6:
            steps.append({'qty': int(parts[1]), 'from' : int(parts[3]), 'to' : int(parts[5])})
          else:
            print("Error: ", line)
        return steps
            

# Function to read lines of a file
def read_lines(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        return lines



# Read a text file's last line and determine the row position for each element space-delimited
def read_last_line(file_name):
    with open(file_name, 'r') as f:
        last_line = f.readlines()[-1]
        #last_line = last_line.split()
        return last_line


# Split string characters into a list
def extract_chars(line):
  newList = {} #[]
  for i in range(len(line)):
    if line[i] != ' ':
      # Create new object
      name = int(line[i])
      newList[name] = {}
      newList[name]["name"] = name
      newList[name]["position"] = i
      newList[name]["items"] = []
  return newList


# ========================================
#fp = os.path.join("day-5", "example-initial-stacks.txt")
#fpSteps = os.path.join("day-5", "example-steps.txt")
fp = os.path.join("day-5", "initial-stacks.txt")
fpSteps = os.path.join("day-5", "steps.txt")

lastLine = read_last_line(fp)
stacks = extract_chars(lastLine)


lines = read_lines(fp)

#Remove last line
lines.pop()

# Enumerate lines in rever
for i, line in enumerate(reversed(lines)):
  #print(i, line)
  for char in stacks:
    if line[stacks[char]["position"]] != ' ':
      stacks[char]["items"].append(line[stacks[char]["position"]])


# Read steps
steps = readSteps(fpSteps)
#print(steps)


puzzlePart = 2 #1 #2


if puzzlePart == 1:
  # ------------------------------------
  # Part 1 - move 1 at a time (reordered)


  # Process the steps on the stacks
  for step in steps:
    for i in range(int(step["qty"])):
      stacks[step["to"]]["items"].append(stacks[step["from"]]["items"].pop())

  #print(stacks)

  # Get last item on each element
  answer = ''
  for stack in stacks:
    # Get last element in each stack list
    answer += stacks[stack]["items"][-1]

  print(answer)


elif puzzlePart == 2:
  # ------------------------------------
  # Part 2 - no reorder when moved

  for step in steps:
    tmp = []
    for i in range(int(step["qty"])):
      tmp.append(stacks[step["from"]]["items"].pop())
      
    # Reverse the list
    tmp.reverse()
    for t in tmp:
      stacks[step["to"]]["items"].append(t)

  answer2 = ''
  for stack in stacks:
    # Get last element in each stack list
    answer2 += stacks[stack]["items"][-1]

  print(answer2)
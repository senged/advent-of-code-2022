# Import libraries needed for reading a file
import os


# Function to read lines of a file 
def readLines(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line)
        return lines



#fp = os.path.join(os.path.dirname(__file__), 'example-input.txt')
fp = os.path.join(os.path.dirname(__file__), 'input.txt')
lines = readLines(fp)

elves = {}
readyForNewElf = True
currentElf = ""

for l in lines:
    
    line = l.strip()

    # is line empty
    if (line == ""):
        readyForNewElf = True
        currentElf = ""

    else:
        if readyForNewElf == True:
            readyForNewElf = False
            #currentElf = "elf" + str(len(elves) + 1)
            currentElf = len(elves) + 1
            elves[currentElf] = []

        elves[currentElf].append(int(line.strip()))


print(elves)

elfSums = {}
maxVal = 0
maxElf = -1
for key, value in elves.items():
    elfSums[key] = sum(value)
    if elfSums[key] > maxVal:
        maxVal = elfSums[key]
        maxElf = key
    elif elfSums[key] == maxVal:
        print("WOAH")

print(elfSums)

max_key = max(elfSums, key=elfSums.get)
print(max_key, maxElf, maxVal)

# Sort dictionary by values descending
sorted_elfSums = sorted(elfSums.items(), key=lambda x: x[1], reverse=True)
top3Sum = 0
for i in range(0,3):
    print(f"Elf {sorted_elfSums[i][0]}: {sorted_elfSums[i][1]}")
    top3Sum += sorted_elfSums[i][1]

print(f"Top 3 elves calories sum: {top3Sum}")
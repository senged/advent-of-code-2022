import os
import numpy as np

def readLines(file):
    with open(file, "r") as f:
        return f.readlines()


def parseLineIntoList(line):
    items = []
    for i in line:
        # Ignore line return
        if i != '\n':
            items.append(int(i))

    return items

def parseRowsIntoColumns(rows):
    columns = []
    for i in range(len(rows[0])):
        columns.append([])
    for row in rows:
        for i in range(len(row)):
            columns[i].append(row[i])
    return columns


def calculateOutsideOfGrid(rows, cols):
    width = len(rows[0])
    height = len(cols[0])
    return 2 * width + 2 * (height - 2)

def calculateScenicScore(rowIdx, colIdx, matrix):
    # Ignore outer edge trees
    if rowIdx == 0 or colIdx == 0 or rowIdx == len(matrix[0,:])-1 or colIdx == len(matrix[:,0])-1:
        return 0

    # Search every direction until:
    #   a) hit the edge
    #   b) hit a tree equal or higher than starting height
    # Caclucate score by multiplying how many steps taken in each direction
    startingHeight = matrix[rowIdx, colIdx]

    maxRowIdx = len(matrix[0,:])
    maxColIdx = len(matrix[:,0])

    # Search left
    scoreLeft = 0
    for idx in range(colIdx-1, -1, -1):
        scoreLeft += 1
        if matrix[rowIdx, idx] >= startingHeight:
            break

    scoreRight = 0
    for idx in range(colIdx+1, maxColIdx):
        scoreRight += 1
        if matrix[rowIdx, idx] >= startingHeight:
            break

    scoreUp = 0
    for idx in range(rowIdx-1, -1, -1):
        scoreUp += 1
        if matrix[idx, colIdx] >= startingHeight:
            break

    scoreDown = 0
    for idx in range(rowIdx+1, maxRowIdx):
        scoreDown += 1
        if matrix[idx, colIdx] >= startingHeight:
            break

    totalScore = scoreLeft * scoreRight * scoreUp * scoreDown
    return totalScore


# ====================================================================================

#fp = os.path.join(os.path.dirname(__file__), "example-input.txt")
fp = os.path.join(os.path.dirname(__file__), "input.txt")
lines = open(fp, "r")


rows = []
for line in lines:
    row = parseLineIntoList(line)
    rows.append(row)


cols = parseRowsIntoColumns(rows)

inputMatrix = np.zeros((len(rows), len(cols)), dtype=int)
for rowIdx in range(0, len(rows)):
    inputMatrix[rowIdx, :] = rows[rowIdx]

# Create a numpy matrix 99 x 99 filled with 0s, then modify outside edges to 1s
matrix = np.zeros((len(rows), len(cols)), dtype=int)
matrix[0,:] = 1
matrix[-1,:] = 1
matrix[:,0] = 1
matrix[:,-1] = 1

# Print the matrix
#print(matrix)
np.savetxt(os.path.join(os.path.dirname(__file__), "output.txt"), matrix, fmt="%d")




# Iterate over each slice of trees, skipping the outer edges to not double count
rowIdx = 0 
for x in rows:

    if (rowIdx == 0 or rowIdx == len(rows)-1):
        rowIdx += 1
        continue

    slice = x

    indexes = list(range(1, len(slice)-1))
    
    # Search Ascending
    previousTree = slice[0]
    for i in indexes:
        if slice[i] > previousTree:
            matrix[rowIdx, i] = 1
            previousTree = slice[i]

        elif slice[i] <= previousTree:
            # If the tree is the same height as or less than the previous tree, 
            # then it is not visible, but doesn't mean we should stop searching.
            # Keep the last highest tree to compare against.
            pass

        else:
            break
    
    # Search Descending
    #slice.reverse()
    indexes = list(range(len(slice)-2 , 0, -1))

    previousTree = slice[len(slice)-1]
    for i in indexes:
        if slice[i] > previousTree:
            matrix[rowIdx, i] = 1
            previousTree = slice[i]

        elif slice[i] <= previousTree:
            pass

        else:
            break

    rowIdx += 1
    np.savetxt(os.path.join(os.path.dirname(__file__), "output.txt"), matrix, fmt="%d")


colIdx = 0 
for x in cols:

    if (colIdx == 0 or colIdx == len(cols)-1):
        colIdx += 1
        continue

    slice = x

    indexes = list(range(1, len(slice)-1))
    
    # Search Ascending
    previousTree = slice[0]
    for i in indexes:
        if slice[i] > previousTree:
            matrix[i, colIdx] = 1
            previousTree = slice[i]

        elif slice[i] <= previousTree:
            pass
        
        else:
            break
    
    # Search Descending
    #slice.reverse()
    indexes = list(range(len(slice)-2 , 0, -1))

    previousTree = slice[len(slice)-1]
    for i in indexes:
        if slice[i] > previousTree:
            matrix[i, colIdx] = 1
            previousTree = slice[i]

        elif slice[i] <= previousTree:
            pass

        else:
            break

    colIdx += 1
    np.savetxt(os.path.join(os.path.dirname(__file__), "output.txt"), matrix, fmt="%d")


print(f"Total trees visible from the outside = {np.sum(matrix)}")
np.savetxt(os.path.join(os.path.dirname(__file__), "output.txt"), matrix, fmt="%d")


# ===================================================
# Part 2 - Cacluate highest scenic score
scenicScoreMatrix = np.zeros((len(rows), len(cols)), dtype=int)

for rowIdx in range(0, len(rows)):
    for colIdx in range(0, len(cols)):
        score = calculateScenicScore(rowIdx, colIdx, inputMatrix)
        scenicScoreMatrix[rowIdx, colIdx] = score


# Find index (row and column) of highest number in numpy matrix
maxIdx = np.unravel_index(np.argmax(scenicScoreMatrix, axis=None), scenicScoreMatrix.shape)

print(f"Max scenic score is ({np.max(scenicScoreMatrix)}) from location {maxIdx}")



import os
import numpy as np

# Read file line by line and split each line into a 2D array
def read_file(file_name):
    with open(file_name) as f:
        return [line.split() for line in f]


# Calculate score for one round
def calculate_score(challenge, response):
    # A(X) = Rock (1), B(Y) = Paper (2), C(Z) = Scissors (3)
    score = 0
    
    if response == 'X': score = 1
    elif response == 'Y': score = 2
    elif response == 'Z': score = 3

    winLoseDraw = -2 #win = 6, draw = 3, lose = 0
    if challenge == 'A':
        if response == 'X': winLoseDraw = 3
        elif response == 'Y': winLoseDraw = 6
        elif response == 'Z' : winLoseDraw = 0
    
    elif challenge == 'B':
        if response == 'X': winLoseDraw = 0
        elif response == 'Y': winLoseDraw = 3
        elif response == 'Z' : winLoseDraw = 6

    elif challenge == 'C':
        if response == 'X': winLoseDraw = 6
        elif response == 'Y': winLoseDraw = 0
        elif response == 'Z' : winLoseDraw = 3        

    score += winLoseDraw
    return score


#fp = os.path.join(os.path.dirname(__file__), "example-input.txt")
fp = os.path.join(os.path.dirname(__file__), "input.txt")

sequence = read_file(fp)
print(sequence)

scores = []
for s in sequence:
    print(s[0], s[1])

    score = calculate_score(s[0], s[1])
    scores.append(score)
    print(f"Challenge = {s[0]}, Response = {s[1]}, Score = {score}")

print(f"Total score = {np.sum(scores)}")


# ======================================================
# Part 2


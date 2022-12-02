with open('Day02/input.txt') as f:
    lines = [line for line in f]

#              "X""Y""Z"  Logic for the first part scoring
scores = {"A": [4, 8, 3],
          "B": [1, 5, 9],
          "C": [7, 2, 6]}

#               "X""Y""Z" Logic for the second part scoring
scores2 = {"A": [3, 4, 8],
           "B": [1, 5, 9],
           "C": [2, 6, 7]}

totalscore = 0
totalscore2 = 0
count = 0

for line in lines:
    me = line.split()[0]
    them = ord(line.split()[1])-88
    score = scores[me][them]
    totalscore = totalscore + score
    score2 = scores2[me][them]
    totalscore2 = totalscore2 + score2
    count = count + 1

print("Part One: " + str(totalscore))
print("Part Two: " + str(totalscore2))
print("Count: " + str(count))

assert totalscore == 11475
assert totalscore2 == 16862
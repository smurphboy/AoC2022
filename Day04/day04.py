with open('Day04/input.txt') as f:
    lines = [line for line in f]

totalcontained = 0
totaloverlap = 0

for line in lines:
    assignments = line.split(',')
    first = assignments[0].split('-')
    second = assignments[1].rstrip().split('-')
    range1 = range(int(first[0]), int(first[1])+1)
    range2 = range(int(second[0]), int(second[1])+1)
    x1 = set(range1)
    x2 = set(range2)
    if len(x1.intersection(x2)) != 0:
        totaloverlap = totaloverlap + 1
    if x1.issubset(range2):
        totalcontained = totalcontained + 1
        continue
    if x2.issubset(range1):
        totalcontained = totalcontained + 1

print("Part One: " + str(totalcontained))
print("Part Two: " + str(totaloverlap))

    

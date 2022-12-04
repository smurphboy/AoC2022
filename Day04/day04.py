with open('Day04/test.txt') as f:
    lines = [line for line in f]

totalcontained = 0

for line in lines:
    assignments = line.split(',')
    first = assignments[0].split('-')
    second = assignments[1].rstrip().split('-')
    print(first, second)
    range1 = range(int(first[0]), int(first[1]))
    range2 = range(int(second[0]), int(second[1]))
    x1 = set(range1)
    if x1.intersection(range2) == x1:
        totalcontained = totalcontained + 1
        print ("1st case")
        continue
    x2 = set(range2)
    if x2.intersection(range1) == x2:
        totalcontained = totalcontained + 1
        print ('2nd case')

print("Part One: " + str(totalcontained))

    

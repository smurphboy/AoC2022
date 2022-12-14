
with open('Day01/input.txt') as f:
    lines = [line for line in f]

elvesfood = []
totalfood = 0
for line in lines:
    if line == '\n':
        elvesfood.append(totalfood)
        totalfood = 0
    else:
        totalfood = totalfood + int(line)

theset = frozenset(elvesfood)
sortedset = sorted(theset, reverse=True)

firstthree = sortedset[0] + sortedset[1] + sortedset[2]
print ('Part One = '+ str(sortedset[0]))
print ('Part Two = ' + str(firstthree))

assert sortedset[0] == 65912
assert firstthree == 195625
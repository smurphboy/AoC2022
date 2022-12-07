import copy
import operator

with open('Day07/input.txt') as f:
    lines = [line.rstrip() for line in f]


currentpath = []
currentdir = ''
dirs = {}
for line in lines:
    if line.split()[0] == "$": #command
        if line.split()[1] == "cd": # cd command
            if line.split()[2] != "..": # append current dir to current path, and add to dirs if not present
                currentpath.append(line.split()[2])
                currentdir = ' '.join(currentpath)
                if currentdir not in dirs:
                    dirs[currentdir] = 0
            else:
                currentpath.pop()
        if line.split()[1] == "ls": # ls command, we can ignore
            pass
    if line.split()[0] == "dir": # dir, so we add if not present to dirs
        currentdir = ' '.join(currentpath)
        currentdir += ' '+line.split()[1]
        if currentdir not in dirs:
            dirs[currentdir] = 0
    if line.split()[0].isnumeric(): # we have a file, add file size to all dirs in current path
        hashcurrentpath = copy.deepcopy(currentpath)
        while len(hashcurrentpath) > 0:
            currentdir = ' '.join(hashcurrentpath)
            dirs[currentdir] = dirs[currentdir] + int(line.split()[0])
            hashcurrentpath.pop()

candidates = []
under100k = 0
under = {}
for dir in dirs:
    if int(dirs[dir]) <= 100000:
        under100k = under100k + int(dirs[dir])
        under[dir] = dirs[dir]
    if int(dirs[dir]) > 3636666:
        candidates.append(int(dirs[dir]))


print("Part One: ", sum(under.values()))
print("Part Two: ", candidates[-1])

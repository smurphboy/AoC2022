with open('Day08/input.txt') as f:
    lines = [line.rstrip() for line in f]

def lefttrees(x,y):
    '''returns if there are taller trees to the left of the current tree, i.e. True means we are hidden'''
    line = forest[y][:]
    if len(line[:x]) > 0:
        tallesttree = max(line[:x])
    else:
        return False
    tree = line[x]
    if tree > tallesttree: # we can be seen
        return False
    else:
        return True

def righttrees(x,y):
    '''returns if there are taller trees to the right of the current tree, i.e. True means we are hidden'''
    line = forest[y][:]
    if len(line[x+1:]) > 0:
        tallesttree = max(line[x+1:])
    else:
        return False
    tree = line[x]
    if tree > tallesttree: # we can be seen
        return False
    else:
        return True

def uptrees(x,y):
    '''returns if there are taller trees above the current tree, i.e. True means we are hidden'''
    treeline = []
    for b, line in enumerate(forest):
        treeline.append(forest[b][x])
    if len(treeline[:y]) > 0:
        tallesttree = max(treeline[:y])
    else:
        return False
    tree = treeline[y]
    if tree > tallesttree: # we can be seen
        return False
    else:
        return True

def downtrees(x,y):
    '''returns if there are taller trees below the current tree, i.e. True means we are hidden'''
    treeline = []
    for b, line in enumerate(forest):
        treeline.append(forest[b][x])
    if len(treeline[y+1:]) > 0:
        tallesttree = max(treeline[y+1:])
    else:
        return False
    tree = treeline[y]
    if tree > tallesttree: # we can be seen
        return False
    else:
        return True

forest = []
for line in lines:
    forest.append([int(x) for x in str(line)])

visibletrees = []

for y, treeline in enumerate(forest):
    for x, tree in enumerate(treeline):
        if lefttrees(x,y) and righttrees(x,y) and uptrees(x,y) and downtrees(x,y):
            pass
        else:
            visibletrees.append([x,y,tree])

print ("Part One: ", str(len(visibletrees)))

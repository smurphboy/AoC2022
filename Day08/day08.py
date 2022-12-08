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

scores = []
for y, treeline in enumerate(forest):
    for x, tree in enumerate(treeline):
        leftscore = 0
        rightscore = 0
        upscore = 0
        downscore = 0
        if x == 0:
            leftscore = 0
        else:
            lefttree = []
            for idx in reversed(range(x)):
                lefttree.append(forest[y][idx])
            for ltree in lefttree:
                if ltree < tree:
                    leftscore = leftscore + 1
                elif ltree >= tree:
                    leftscore = leftscore + 1
                    break
        if x == len(treeline)-1:
            rightscore = 0
        else:
            righttree = []
            for idx in range(x+1,len(forest[0])):
                righttree.append(forest[y][idx])
            for rtree in righttree:
                if rtree < tree:
                    rightscore = rightscore + 1
                elif rtree >= tree:
                    rightscore = rightscore + 1
                    break
        if y == 0:
            upscore = 0
        else:
            uptree = []
            for idx in reversed(range(y)):
                uptree.append(forest[idx][x])
            for utree in uptree:
                if utree < tree:
                    upscore = upscore + 1
                if utree >= tree:
                    upscore = upscore + 1
                    break
        if y == len(forest[0])-1:
            downscore = 0
        else:
            downtree = []
            for idx in range(y+1, len(forest[0])):
                downtree.append(forest[idx][x])
            for dtree in downtree:
                if dtree < tree:
                    downscore = downscore + 1
                if dtree >= tree:
                    downscore = downscore + 1
                    break
        totalscore = leftscore * rightscore * upscore * downscore
        scores.append([x,y,tree,leftscore,rightscore,upscore,downscore,totalscore])

print ("Part One: ", str(len(visibletrees)))
print ("Part Two: ", max(sublist[7] for sublist in scores))
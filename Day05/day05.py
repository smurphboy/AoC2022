import copy

with open('Day05/input.txt') as f:
    lines = [line.rstrip() for line in f]

stacks = [[],[],[],[],[],[],[],[],[]]
moves = []

for line in lines:
    if len(line) > 0: # above the numbers 
        if line[0] == "[": # we are in the stack
            for pos, char in enumerate(line):
                if char != "[" and char != "]" and char != " ": # we have a stack item or a blank
                    stacks[int((pos+3)/4)-1].append(char)
    if line[:4] == "move":
        movelist = line.split(' ')
        moves.append(movelist)

for stack in stacks:
    stack.reverse()

stacks2 = copy.deepcopy(stacks) # make a copy for part two

for move in moves:
    movecount = int(move[1])
    while movecount > 0:
        stacks[int(move[5])-1].append(stacks[int(move[3])-1].pop())
        movecount = movecount - 1

for move in moves:
    crates2move = stacks2[int(move[3])-1][-int(move[1]):]
    for crate in crates2move:
        stacks2[int(move[5])-1].append(crate)
    for crate in crates2move:
        stacks2[int(move[3])-1].pop()


partone = ""
stacktop = []
for stack in stacks:
    stacktop.append(stack[-1])

parttwo = ""
stack2top = []
for stack in stacks2:
    stack2top.append(stack[-1])

print("Part One: ", partone.join(stacktop))
print("Part Two: ", partone.join(stack2top))
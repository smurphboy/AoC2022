with open('Day10/input.txt') as f:
    lines = [line.rstrip() for line in f]

cycle = 0
x = 1
signalstrength = []

for command in lines:
    if command.split()[0] == "noop":
        cycle += 1
        signalstrength.append([cycle, x])
    if command.split()[0] == "addx":
        cycle += 1
        signalstrength.append([cycle, x])
        cycle += 1
        x = x + int(command.split()[1])
        signalstrength.append([cycle, x])

# for idx, cycle in enumerate(signalstrength):
#     print(cycle[0], cycle[1], (cycle[0] * signalstrength[idx-1][1]))

def strength(cycle):
    return ([signalstrength[cycle-1][0], signalstrength[cycle-2][1], int(signalstrength[cycle-1][0]) * int(signalstrength[cycle-2][1])])

print(strength(20))
print(strength(60))
print(strength(100))
print(strength(140))
print(strength(180))
print(strength(220))
strenghts = [strength(20)[2], strength(60)[2], strength(100)[2], strength(140)[2], strength(180)[2], strength(220)[2]]
print("Part One: ", sum(strenghts))
assert sum(strenghts) == 13480

pic = []
line = ""
for cycle, x in enumerate(sublist[:2] for sublist in signalstrength):
    print(cycle, x[1])
    if (cycle % 40) == 0:
        line = line + "#"
    if abs(((cycle+1) % 40) - int(x[1])) < 2 :
        line = line + "#"
    else:
        line = line + "."
    if (cycle+1) % 40 == 0:
        pic.append(line)
        line = ""

for line in pic:
    print (line)

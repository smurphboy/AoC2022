import math

with open('Day11/input.txt') as f:
    lines = [line.rstrip() for line in f]

monkeysdata = []
monkeydata = []

for line in lines:
    if len(line) == 0:
        pass
    elif line.split()[0] == "Monkey":
        if int(line.split()[1][0]) != 0:
            monkeysdata.append(monkeydata)
            monkeydata = []
        currentmonkey = int(line.split()[1][0])
        monkeydata.append(currentmonkey)
    elif line.split()[0] == "Starting":
        items = []
        for item in line.split()[2:]:
            items.append(item.rstrip(","))
        monkeydata.append(items)
    elif line.split()[0] == "Operation:":
        monkeydata.append(line.split()[4])
        monkeydata.append(line.split()[5])
    elif line.split()[0] == "Test:":
        monkeydata.append(line.split()[3])
    elif line.split()[1] == "true:":
        monkeydata.append(int(line.split()[5]))
    elif line.split()[1] == "false:":
        monkeydata.append(int(line.split()[5])) 
monkeysdata.append(monkeydata)       

print(monkeysdata)
inspections = {}
for monkey in monkeysdata:
    inspections[str(monkey[0])] = 0

def part(rounds, worryfactor, md, inspect):
    for round in range(rounds):
        print(round)
        for idx, monkey in enumerate(md):
            for idx2 in range(len(md[idx][1])):
                inspect[str(idx)] += 1
                if md[idx][3] == "old":
                    md[idx][1][0] = (int(md[idx][1][0]) ** 2) // worryfactor
                elif (md[idx][3] != "old") and (md[idx][2] == "*"):
                    md[idx][1][0] = (int(md[idx][1][0]) * int(md[idx][3])) // worryfactor
                elif (md[idx][3] != "old") and (md[idx][2] == "+"):
                    md[idx][1][0] = (int(md[idx][1][0]) + int(md[idx][3])) // worryfactor
                if int(md[idx][1][0]) % int(md[idx][4]) == 0:
                    md[md[idx][5]][1].append(md[idx][1].pop(0))
                else:
                    md[md[idx][6]][1].append(md[idx][1].pop(0))
    return inspect

inspections = part(20, 3, monkeysdata, inspections)
print (inspections)
        
print("Part One :", (sorted(inspections.values())[-2] * sorted(inspections.values())[-1]))

inspections = {}
for monkey in monkeysdata:
    inspections[str(monkey[0])] = 0

inspections = part(10000, 1, monkeysdata, inspections)
print (inspections)
        
print("Part Two :", (sorted(inspections.values())[-2] * sorted(inspections.values())[-1]))
with open('Day06/input.txt') as f:
    lines = [line.rstrip() for line in f]

packetstart = []
packetmarker = 1

for line in lines:
    for char in line:
        if len(packetstart) < 4: # we just add the char
            packetstart.append(char)
            packetmarker = packetmarker + 1
            continue
        else: # we have 4 in the buffer already
            packetstart.pop(0)
            packetstart.append(char)
        if len(set(packetstart)) == len(packetstart): # we have unique characters
            break
        packetmarker = packetmarker + 1

messagestart = []
messagemarker = 1

for line in lines:
    for char in line:
        if len(messagestart) < 14: # we just add the char
            messagestart.append(char)
            messagemarker = messagemarker + 1
            continue
        else: # we have 4 in the buffer already
            messagestart.pop(0)
            messagestart.append(char)
        if len(set(messagestart)) == len(messagestart): # we have unique characters
            break
        messagemarker = messagemarker + 1

print("Part One: " + str(packetmarker))
print("Part One: " + str(messagemarker))
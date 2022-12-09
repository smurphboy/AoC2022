import copy

with open('Day09/input.txt') as f:
    lines = [line.rstrip() for line in f]

hpx = 0
hpy = 0
tpx = 0
tpy = 0
trail = [(0,0)]

def resolvetail(hposx, hposy, tposx, tposy):
    '''resolve tail position'''
    if (abs(hposx - tposx) <= 1) and (abs(hposy - tposy) <=1):
        return (hposx,hposy,tposx,tposy)
    elif ((hposx - tposx) == 2) and (hposy == tposy): # move right
        tposx = tposx + 1
    elif ((hposx - tposx) == -2) and (hposy == tposy): # move left
        tposx = tposx - 1
    elif ((hposy - tposy) == 2) and (hposx == tposx): # move up
        tposy = tposy + 1
    elif ((hposy - tposy) == -2) and (hposx == tposx): # move down
        tposy = tposy - 1
    elif ((hposx - tposx) == 2) and ((hposy - tposy) == 2):
        tposx = tposx + 1
        tposy = tposy + 1
    elif ((hposx - tposx) == -2) and ((hposy - tposy) == 2):
        tposx = tposx - 1
        tposy = tposy + 1
    elif ((hposx - tposx) == 2) and ((hposy - tposy) == -2):
        tposx = tposx + 1
        tposy = tposy - 1
    elif ((hposx - tposx) == -2) and ((hposy - tposy) == -2):
        tposx = tposx - 1
        tposy = tposy - 1
    elif ((hposx - tposx) == 1) and ((hposy - tposy) == 1):
        return (hposx,hposy,tposx,tposy)
    elif ((hposx - tposx) == -1) and ((hposy - tposy) == 1):
        return (hposx,hposy,tposx,tposy)
    elif ((hposx - tposx) == 1) and ((hposy - tposy) == -1):
        return (hposx,hposy,tposx,tposy)
    elif ((hposx - tposx) == -1) and ((hposy - tposy) == -1):
        return (hposx,hposy,tposx,tposy)
    elif ((hposx - tposx) == 2) and ((hposy - tposy) == 1):
        tposx = tposx + 1
        tposy = tposy + 1
    elif ((hposx - tposx) == 1) and ((hposy - tposy) == 2):
        tposx = tposx + 1
        tposy = tposy + 1
    elif ((hposx - tposx) == -2) and ((hposy - tposy) == 1):
        tposx = tposx - 1
        tposy = tposy + 1
    elif ((hposx - tposx) == -1) and ((hposy - tposy) == 2):
        tposx = tposx - 1
        tposy = tposy + 1
    elif ((hposx - tposx) == -2) and ((hposy - tposy) == -1):
        tposx = tposx - 1
        tposy = tposy - 1
    elif ((hposx - tposx) == -1) and ((hposy - tposy) == -2):
        tposx = tposx - 1
        tposy = tposy - 1
    elif ((hposx - tposx) == 2) and ((hposy - tposy) == -1):
        tposx = tposx + 1
        tposy = tposy - 1
    elif ((hposx - tposx) == 1) and ((hposy - tposy) == -2):
        tposx = tposx + 1
        tposy = tposy - 1
    else:
        print('oops')
    trail.append((tposx,tposy))       
    #print(hposx,hposy,tposx,tposy)
    return (hposx,hposy,tposx,tposy)
    
moves = []
for move in lines:
    moves.append(move.split())

for move in moves:
    for idx in range(int(move[1])):
        if move[0] == "R":
            hpx = hpx + 1
        if move[0] == "L":
            hpx = hpx - 1
        if move[0] == "U":
            hpy = hpy + 1
        if move[0] == "D":
            hpy = hpy - 1
        newpos = resolvetail(hpx, hpy, tpx, tpy)
        hpx = newpos[0]
        hpy = newpos[1]
        tpx = newpos[2]
        tpy = newpos[3]

trail = set(trail)
print("Part One :", len(trail))
assert len(trail) == 5513
trail=[(0,0)]

hpx = 0
hpy = 0
tpx2 = [0,0,0,0,0,0,0,0,0]
tpy2 = [0,0,0,0,0,0,0,0,0]
trail2 = [(0,0)]
      
for move in moves:
    for idx in range(int(move[1])):
        if move[0] == "R":
            hpx = hpx + 1
        if move[0] == "L":
            hpx = hpx - 1
        if move[0] == "U":
            hpy = hpy + 1
        if move[0] == "D":
            hpy = hpy - 1
        for idx2 in range(9):
            if idx2 == 0:
                newpos = resolvetail(hpx, hpy, tpx2[0], tpy2[0])
                hpx = newpos[0]
                hpy = newpos[1]
                tpx2[0] = newpos[2]
                tpy2[0] = newpos[3]
            else:
                newpos = resolvetail(tpx2[(idx2)-1], tpy2[(idx2)-1], tpx2[idx2], tpy2[idx2])
                tpx2[(idx2)-1] = newpos[0]
                tpy2[(idx2)-1] = newpos[1]
                tpx2[idx2] = newpos[2]
                tpy2[idx2] = newpos[3]
        trail2.append((tpx2[8],tpy2[8]))

trail2 = set(trail2)

print("Part Two :", len(trail2))
assert len(trail2) == 2427

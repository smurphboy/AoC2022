try:
   from itertools import izip_longest
except ImportError:  # Python 3
    from itertools import zip_longest as izip_longest
from textwrap import wrap

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)
with open('Day03/input.txt') as f:
    lines = [line for line in f]

totalpriority = 0

for line in lines:
    splitpoint = int((len(line)-1)/2)
    compartments = wrap(line, splitpoint)
    setone = set([letter for letter in compartments[0]])
    settwo = ([letter for letter in compartments[1]])
    common = setone.intersection(settwo)
    common = list(common)[0]
    if common[0].islower():
        totalpriority = totalpriority + ord(common[0])-96
    else:
        totalpriority = totalpriority + ord(common[0])-38

totalpriority2 = 0

with open('Day03/input.txt') as f:
    for lines in grouper(f, 3, ''):
        assert len(lines) == 3
        # process N lines here
        sets = [set(line) for line in lines]
        common = sets[0].intersection(sets[1].intersection(sets[2]))
        common.remove('\n')
        common = list(common)[0]
        if common[0].islower():
            totalpriority2 = totalpriority2 + ord(common[0])-96
        else:
            totalpriority2 = totalpriority2 + ord(common[0])-38


print("Part One: " + str(totalpriority))
print("Part Two: " + str(totalpriority2))
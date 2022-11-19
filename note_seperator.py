def noteSeperator(filename):
    f = open(filename, 'r')
    notes = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    lines = f.readlines()
    for line in lines:
        seperate = line.replace('\n', "").replace(" ", "").split(",")
        notes[int(seperate[0]) % 48].append((str(seperate[1]),str(seperate[2])))
    f.close()
    return notes

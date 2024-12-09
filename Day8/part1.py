import numpy as np;

input = open("Day8/input.txt", "r")
input=input.readlines()
input = list(map(lambda a: a.strip(), input))
antennas={}
MAX_HEIGHT = len(input)
MAX_WIDTH = len(input[0])
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] != '.':
            if input[i][j] not in antennas:
                antennas[input[i][j]] = [(i,j)]
            else:
                antennas[input[i][j]].append((i,j))

antinodes=[]
for antenna in antennas:
    locations=antennas[antenna]
    
    for i in range(len(locations)-1):
        y = np.asarray(locations[i], dtype=np.int64)
        for j in range(i+1,len(locations)):
            z = np.asarray(locations[j], dtype=np.int64)
            x = y+2*(z-y)
            x = tuple(map(int, x))
            if(x[0] < MAX_HEIGHT and x[0] > -1 and x[1] < MAX_WIDTH and x[1] > -1 and x not in antinodes):
                antinodes.append(x)
            x = y+(-1)*(z-y)
            x = tuple(map(int, x))
            if(x[0] < MAX_HEIGHT and x[0] > -1 and x[1] < MAX_WIDTH and x[1] > -1 and x not in antinodes):
                antinodes.append(x)
print(antinodes)
print(len(antinodes))

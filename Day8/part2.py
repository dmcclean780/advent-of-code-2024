import numpy as np;

input = open("Day8/input.txt", "r")
input=input.readlines()
input = list(map(lambda a: a.strip(), input))
antennas={}
MAX_HEIGHT = len(input)-1
MAX_WIDTH = len(input[0])-1
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
        a = locations[i]
        
        for j in range(i+1,len(locations)):
            z = locations[j]
            dx = a[1] - z[1]
            dy = a[0] - z[0]
            
            # Create a list to store integer points within the bounds
            # Determine the step size for x
            if dx != 0:
                t_step = 1 / abs(dx)  # step in t for each unit change in x
            
            # Loop through the possible x values within the range
            for x in range(0, MAX_WIDTH + 1):
               
                t = (x - a[1]) / dx if dx != 0 else 0  # For vertical lines, t doesn't depend on x
                
                y = a[0] + t * dy

                # If y is an integer and within the y-boundaries, add the point
                if 0 <= y <= MAX_HEIGHT and y.is_integer() and (x, int(y)) not in antinodes:
                    antinodes.append((x, int(y)))
            
            # If dx is 0, then handle vertical lines separately by using the same approach on y.
            if dx == 0:
                for y in range(0, MAX_HEIGHT + 1):
                    if (a[0], y) not in antinodes:
                        antinodes.append((a[0], y))

print(antinodes)
print(len(antinodes))

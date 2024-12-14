import math

def mean_nearest_neighbor_distance(points):
    n = len(points)
    total_nearest_distance = 0  # Sum of all nearest neighbor distances

    for i, (x1, y1) in enumerate(points):
        min_distance = float('inf')  # Initialize minimum distance

        for j, (x2, y2) in enumerate(points):
            if i != j:  # Avoid self-comparison
                distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  # Euclidean distance
                min_distance = min(min_distance, distance)  # Track minimum distance
        
        total_nearest_distance += min_distance  # Add nearest distance to total
    
    mean_distance = total_nearest_distance / n  # Compute mean nearest neighbor distance
    return mean_distance

data = open("Day14/input.txt", "r")
data = list(map( lambda a:a.strip(), data.readlines()))
data = list(map( lambda a: a.split(' '), data))
bots=[]
size=(101,103)
for j in data:
    pos = tuple(map(lambda a: int(a), j[0].split('p=')[-1].split(',')))
    vel = tuple(map(lambda a: int(a), j[1].split('v=')[-1].split(',')))
    bot = [pos, vel]
    bots.append(bot)

time = 100
updatedPositions=[]
treeFrame=0
minMeanNearestNeighbour=-1
for i in range(10000):
    updatedPositions=set()
    for j in range(len(bots)):
        pos = bots[j][0]
        v=bots[j][1]
        newPosX = pos[0]+v[0]
        while newPosX < 0:
            newPosX = size[0]+newPosX
        while newPosX >= size[0]:
            newPosX = newPosX-size[0]
        
        newPosY = pos[1]+v[1]
        while newPosY < 0:
            newPosY = size[1]+newPosY
        while newPosY >= size[1]:
            newPosY = newPosY-size[1]
        
        newPos=(newPosX, newPosY)
        bots[j][0]=newPos
        updatedPositions.add(newPos)
    grid=""
    if(len(updatedPositions)==len(bots)):
        for j in range(size[1]):
            for k in range(size[0]):
                if (k,j) in updatedPositions:
                    grid+='#'
                else:
                    grid+='.'
            grid+='\n'

        print(grid)
        print(i)
        x=input("wait")
perimerters={}
areas={}
visitedLocations=[]
def mapRegion(letter, startingLocation, WIDTH, HEIGHT, map):
    locationsToVisit=[startingLocation]
    area = 0
    perimeter = 0
    visitedLocationsOfLetter=[]
    while(len(locationsToVisit) != 0):
        location = locationsToVisit.pop()
        area+=1
        visitedLocations.append(location)
        visitedLocationsOfLetter.append(location)
        up = (location[0]-1, location[1]) if location[0]-1 > -1 else None
        down = (location[0]+1, location[1]) if location[0]+1 < HEIGHT else None
        left = (location[0], location[1]-1) if location[1]-1 > -1 else None
        right = (location[0], location[1]+1) if location[1]+1 < WIDTH else None
        if(up not in visitedLocationsOfLetter):
            if up != None and map[up[0]][up[1]] == letter:
                if up not in locationsToVisit: locationsToVisit.append(up)
            else:
                perimeter+=1
        if(down not in visitedLocationsOfLetter):
            if down != None and map[down[0]][down[1]] == letter:
               
                if down not in locationsToVisit: locationsToVisit.append(down)
            else:
                perimeter+=1
        if(left not in visitedLocationsOfLetter):
            if left != None and map[left[0]][left[1]] == letter:
               
                if left not in locationsToVisit: locationsToVisit.append(left)
            else:
                perimeter+=1
        if(right not in visitedLocationsOfLetter):
            if right != None and map[right[0]][right[1]] == letter:
               
                if right not in locationsToVisit: locationsToVisit.append(right)
            else:
                perimeter+=1
    if( letter not in perimerters):
        perimerters[letter]=[perimeter]
        areas[letter]=[area]
    else:
        perimerters[letter].append(perimeter)
        areas[letter].append(area)



input = open("Day12/input.txt", "r")
input=list(map(lambda a: a.strip(), input.readlines()))

WIDTH = len(input[0])
HEIGHT = len(input)
for i in range(len(input)):
    for j in range(len(input[i])):
        location = (i,j)
        letter=input[i][j]
        if(location not in visitedLocations):
            mapRegion(letter, location, WIDTH, HEIGHT, input)
            print(letter)
            print(areas[letter])
            print(perimerters[letter])
            print('\n')

total=0
for i in perimerters:
    perimerterSections=perimerters[i]
    areaSections=areas[i]
    for j in range(len(perimerterSections)):
        p=perimerterSections[j]
        a=areaSections[j]
        price = a*p
        total+=price

print(total)
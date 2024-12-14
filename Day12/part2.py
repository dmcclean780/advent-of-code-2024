def count_missing_gaps(sequence):
    if not sequence:
        return 0

    # Sort the sequence to ensure proper order
    sequence = sorted(sequence)

    # Initialize a counter for missing gaps
    missing_gaps = 0

    # Iterate through the sequence and check for gaps
    for i in range(len(sequence) - 1):
        if sequence[i + 1] - sequence[i] > 1:
            missing_gaps += 1

    return missing_gaps


perimerters={}
areas={}
visitedLocations=[]
def mapRegion(letter, startingLocation, WIDTH, HEIGHT, map):
    locationsToVisit=[startingLocation]
    area = 0
    perimeter = 0
    visitedLocationsOfLetter=[]
    upSides={}
    downSides={}
    leftSides={}
    rightSides={}
    while(len(locationsToVisit) != 0):
        location = locationsToVisit.pop()
        area+=1
        visitedLocations.append(location)
        visitedLocationsOfLetter.append(location)
        up = (location[0]-1, location[1]) 
        down = (location[0]+1, location[1]) 
        left = (location[0], location[1]-1) 
        right = (location[0], location[1]+1)
        if(up not in visitedLocationsOfLetter):
            #print(up)
            if up[0] > -1 and map[up[0]][up[1]] == letter:
                if up not in locationsToVisit: locationsToVisit.append(up)
            else:
                if(up[0] not in upSides):
                    upSides[up[0]]=[up[1]]
                else:
                    upSides[up[0]].append(up[1])
        if(down not in visitedLocationsOfLetter):
            #print(down)
            if down[0] < HEIGHT and map[down[0]][down[1]] == letter:
               
                if down not in locationsToVisit: locationsToVisit.append(down)
            else:
                if(down[0] not in downSides):
                    downSides[down[0]]=[down[1]]
                else:
                    downSides[down[0]].append(down[1])
        if(left not in visitedLocationsOfLetter):
            #print(left)
            if left[1] >-1 and map[left[0]][left[1]] == letter:
               
                if left not in locationsToVisit: locationsToVisit.append(left)
            else:
                if(left[1] not in leftSides):
                    leftSides[left[1]]=[left[0]]
                else:
                    leftSides[left[1]].append(left[0])
        if(right not in visitedLocationsOfLetter):
            #print(right)
            if right[1] < WIDTH and map[right[0]][right[1]] == letter:
               
                if right not in locationsToVisit: locationsToVisit.append(right)
            else:
                if(right[1] not in rightSides):
                    rightSides[right[1]]=[right[0]]
                else:
                    rightSides[right[1]].append(right[0])
    # print(letter)
    totalSides=0
    for i in upSides:
        sides = count_missing_gaps(upSides[i])
        sides+=1
        totalSides+=sides
    print(totalSides)
    for i in downSides:
        sides = count_missing_gaps(downSides[i])
        sides+=1
        totalSides+=sides
    print(totalSides)
    for i in leftSides:
        print(leftSides)
        sides = count_missing_gaps(leftSides[i])
        print(sides)
        sides+=1
        totalSides+=sides
    print(totalSides)
    for i in rightSides:
        sides = count_missing_gaps(rightSides[i])
        sides+=1
        totalSides+=sides
    print(totalSides)
    if( letter not in perimerters):
        perimerters[letter]=[totalSides]
        areas[letter]=[area]
    else:
        perimerters[letter].append(totalSides)
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
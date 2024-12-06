import copy

def checkForLoop(puzzle, currentPos):
    upTurns=[]
    rightTurns=[]
    downTurns=[]
    leftTurns=[]
    while(True):
        #print(currentPos)
        #print(puzzle[currentPos[0]][currentPos[1]])
        if(puzzle[currentPos[0]][currentPos[1]] == '^'):
            nextPos = (currentPos[0]-1, currentPos[1])
            if(nextPos[0] < 0):
                return False
            if(puzzle[nextPos[0]][nextPos[1]] == '.'):
                puzzle[nextPos[0]][nextPos[1]] = '^'
                currentPos=nextPos
                pathPos.append(nextPos)
                continue
            if(puzzle[nextPos[0]][nextPos[1]] == '^' or puzzle[nextPos[0]][nextPos[1]] == '>' or puzzle[nextPos[0]][nextPos[1]] == 'v' or puzzle[nextPos[0]][nextPos[1]] == '<'):
                puzzle[nextPos[0]][nextPos[1]] = '^'
                currentPos=nextPos
                continue
            if(puzzle[nextPos[0]][nextPos[1]] == '#'):
                if(currentPos in upTurns):
                    return True
                upTurns.append(currentPos)
                puzzle[currentPos[0]][currentPos[1]] = '>'
        if(puzzle[currentPos[0]][currentPos[1]] == '>'):
            nextPos = (currentPos[0], currentPos[1]+1)
            if(nextPos[1] >= len(puzzle[0])):
                return False
            if(puzzle[nextPos[0]][nextPos[1]] == '.'):
                puzzle[nextPos[0]][nextPos[1]] = '>'
                currentPos=nextPos
                pathPos.append(nextPos)
                continue
            if(puzzle[nextPos[0]][nextPos[1]] == '^' or puzzle[nextPos[0]][nextPos[1]] == '>' or puzzle[nextPos[0]][nextPos[1]] == 'v' or puzzle[nextPos[0]][nextPos[1]] == '<'):
                puzzle[nextPos[0]][nextPos[1]] = '>'
                currentPos=nextPos
                continue
            if(puzzle[nextPos[0]][nextPos[1]] == '#'):
                if(currentPos in rightTurns):
                    return True
                rightTurns.append(currentPos)
                puzzle[currentPos[0]][currentPos[1]] = 'v'
        if(puzzle[currentPos[0]][currentPos[1]] == 'v'):
            nextPos = (currentPos[0]+1, currentPos[1])
            if(nextPos[0] >= len(puzzle)):
                return False
            if(puzzle[nextPos[0]][nextPos[1]] == '.'):
                puzzle[nextPos[0]][nextPos[1]] = 'v'
                currentPos=nextPos
                pathPos.append(nextPos)
                continue
            if(puzzle[nextPos[0]][nextPos[1]] == '^' or puzzle[nextPos[0]][nextPos[1]] == '>' or puzzle[nextPos[0]][nextPos[1]] == 'v' or puzzle[nextPos[0]][nextPos[1]] == '<'):
                puzzle[nextPos[0]][nextPos[1]] = 'v'
                currentPos=nextPos
                continue
            if(puzzle[nextPos[0]][nextPos[1]] == '#'):
                if(currentPos in downTurns):
                    return True
                downTurns.append(currentPos)
                puzzle[currentPos[0]][currentPos[1]] = '<'
        if(puzzle[currentPos[0]][currentPos[1]] == '<'):
            nextPos = (currentPos[0], currentPos[1]-1)
            if(nextPos[1] < 0):
                return False
            if(puzzle[nextPos[0]][nextPos[1]] == '.'):
                puzzle[nextPos[0]][nextPos[1]] = '<'
                currentPos=nextPos
                pathPos.append(nextPos)
                continue
            if(puzzle[nextPos[0]][nextPos[1]] == '^' or puzzle[nextPos[0]][nextPos[1]] == '>' or puzzle[nextPos[0]][nextPos[1]] == 'v' or puzzle[nextPos[0]][nextPos[1]] == '<'):
                puzzle[nextPos[0]][nextPos[1]] = '<'
                currentPos=nextPos
                continue
            if(puzzle[nextPos[0]][nextPos[1]] == '#'):
                if(currentPos in leftTurns):
                    return True
                leftTurns.append(currentPos)
                puzzle[currentPos[0]][currentPos[1]] = '^'


input = open("Day6/input.txt", "r")
original=input.readlines()
for i in range(len(original)):
    original[i]=list(original[i].strip())
for i in range(len(original)):
    for j in range(len(original[i])):
        if(original[i][j] == '^' or original[i][j] == '>' or original[i][j] == 'v' or original[i][j] == '<'):
            startPos=(i,j)
            currentPos=startPos
            break
pathPos = []
puzzle=copy.deepcopy(original)
while(True):
    if(puzzle[currentPos[0]][currentPos[1]] == '^'):
        nextPos = (currentPos[0]-1, currentPos[1])
        if(nextPos[0] < 0):
            break
        if(puzzle[nextPos[0]][nextPos[1]] == '.'):
            puzzle[nextPos[0]][nextPos[1]] = '^'
            currentPos=nextPos
            pathPos.append(nextPos)
            continue
        if(puzzle[nextPos[0]][nextPos[1]] == '^' or puzzle[nextPos[0]][nextPos[1]] == '>' or puzzle[nextPos[0]][nextPos[1]] == 'v' or puzzle[nextPos[0]][nextPos[1]] == '<'):
            puzzle[nextPos[0]][nextPos[1]] = '^'
            currentPos=nextPos
            continue
        if(puzzle[nextPos[0]][nextPos[1]] == '#'):
            puzzle[currentPos[0]][currentPos[1]] = '>'
    if(puzzle[currentPos[0]][currentPos[1]] == '>'):
        nextPos = (currentPos[0], currentPos[1]+1)
        if(nextPos[1] >= len(puzzle[0])):
            break
        if(puzzle[nextPos[0]][nextPos[1]] == '.'):
            puzzle[nextPos[0]][nextPos[1]] = '>'
            currentPos=nextPos
            pathPos.append(nextPos)
            continue
        if(puzzle[nextPos[0]][nextPos[1]] == '^' or puzzle[nextPos[0]][nextPos[1]] == '>' or puzzle[nextPos[0]][nextPos[1]] == 'v' or puzzle[nextPos[0]][nextPos[1]] == '<'):
            puzzle[nextPos[0]][nextPos[1]] = '>'
            currentPos=nextPos
            continue
        if(puzzle[nextPos[0]][nextPos[1]] == '#'):
            puzzle[currentPos[0]][currentPos[1]] = 'v'
    if(puzzle[currentPos[0]][currentPos[1]] == 'v'):
        nextPos = (currentPos[0]+1, currentPos[1])
        if(nextPos[0] >= len(puzzle)):
            break
        if(puzzle[nextPos[0]][nextPos[1]] == '.'):
            puzzle[nextPos[0]][nextPos[1]] = 'v'
            currentPos=nextPos
            pathPos.append(nextPos)
            continue
        if(puzzle[nextPos[0]][nextPos[1]] == '^' or puzzle[nextPos[0]][nextPos[1]] == '>' or puzzle[nextPos[0]][nextPos[1]] == 'v' or puzzle[nextPos[0]][nextPos[1]] == '<'):
            puzzle[nextPos[0]][nextPos[1]] = 'v'
            currentPos=nextPos
            continue
        if(puzzle[nextPos[0]][nextPos[1]] == '#'):
            puzzle[currentPos[0]][currentPos[1]] = '<'
    if(puzzle[currentPos[0]][currentPos[1]] == '<'):
        nextPos = (currentPos[0], currentPos[1]-1)
        if(nextPos[1] < 0):
            break
        if(puzzle[nextPos[0]][nextPos[1]] == '.'):
            puzzle[nextPos[0]][nextPos[1]] = '<'
            currentPos=nextPos
            pathPos.append(nextPos)
            continue
        if(puzzle[nextPos[0]][nextPos[1]] == '^' or puzzle[nextPos[0]][nextPos[1]] == '>' or puzzle[nextPos[0]][nextPos[1]] == 'v' or puzzle[nextPos[0]][nextPos[1]] == '<'):
            puzzle[nextPos[0]][nextPos[1]] = '<'
            currentPos=nextPos
            continue
        if(puzzle[nextPos[0]][nextPos[1]] == '#'):
            puzzle[currentPos[0]][currentPos[1]] = '^'

loops=0
#rint(startPos)
#print(original)
for i in range(len(pathPos)):
    newObsticalPosition = pathPos[i]
    #print(newObsticalPosition)
    thisRoom = copy.deepcopy(original)
    #print(thisRoom)
    thisRoom[newObsticalPosition[0]][newObsticalPosition[1]]='#' 
    if(checkForLoop(thisRoom, startPos)):
        loops+=1
        #print(loops)
    
print(loops)
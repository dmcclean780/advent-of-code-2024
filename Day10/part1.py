input = open("Day10/input.txt", "r")
input=input.readlines()
input=map(lambda a: a.strip(), input)

map=[]
for x in input:
    row=[]
    for y in x:
        if(y != '.'):
            row.append(int(y))
        else:
            row.append(-1)
    map.append(row)


def walkPath(position, value, foundNines):
    nines=0
    up=(position[0]-1, position[1])
    down=(position[0]+1, position[1])
    left=(position[0], position[1]-1)
    right=(position[0], position[1]+1)
    if(value == 8):
        if(up[0]>-1 and map[up[0]][up[1]] == 9 and up not in foundNines):
            nines+=1
            foundNines.append(up)
        if(down[0]<len(map) and map[down[0]][down[1]] == 9 and down not in foundNines):
            nines+=1
            foundNines.append(down)
        if(left[1]>-1 and map[left[0]][left[1]] == 9 and left not in foundNines):
            nines+=1
            foundNines.append(left)
        if(right[1]<len(map[0]) and map[right[0]][right[1]] == 9 and right not in foundNines):
            nines+=1
            foundNines.append(right)
    else:
        #print(value, up, value+1, map[up[0]][up[1]])
        if(up[0]>-1 and map[up[0]][up[1]] == value+1):
            nines+=walkPath(up, value+1, foundNines)
        #print(value, down, value+1, map[down[0]][down[1]])
        if(down[0]<len(map) and map[down[0]][down[1]] == value+1):
            nines+=walkPath(down, value+1, foundNines)
        #print(value, left, value+1, map[left[0]][left[1]])
        if(left[1]>-1 and map[left[0]][left[1]] == value+1):
            nines+=walkPath(left, value+1, foundNines)
        #print(value, right, value+1, map[right[0]][right[1]])
        if(right[1]<len(map[0]) and map[right[0]][right[1]] == value+1):
            nines+=walkPath(right, value+1, foundNines)
    #print(value, nines)
    return nines


total=0
for i in range(len(map)):
    for j in range(len(map)):
        if(map[i][j] == 0):
            position=(i,j)
            foundNines = []
            total+=walkPath(position, 0, foundNines)
print(total)
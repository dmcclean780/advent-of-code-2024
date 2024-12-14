input = open("Day14/input.txt", "r")
input = list(map( lambda a:a.strip(), input.readlines()))
input = list(map( lambda a: a.split(' '), input))
bots=[]
size=(101,103)
for i in input:
    pos = tuple(map(lambda a: int(a), i[0].split('p=')[-1].split(',')))
    vel = tuple(map(lambda a: int(a), i[1].split('v=')[-1].split(',')))
    bot = [pos, vel]
    bots.append(bot)
print(bots)

time = 100
updatedPositions=[]
for bot in bots:
    pos = bot[0]
    v=bot[1]
    newPosX = pos[0]+time*v[0]
    while newPosX < 0:
        newPosX = size[0]+newPosX
    while newPosX >= size[0]:
        newPosX = newPosX-size[0]
    
    newPosY = pos[1]+time*v[1]
    print(newPosY)
    while newPosY < 0:
        newPosY = size[1]+newPosY
    while newPosY >= size[1]:
        newPosY = newPosY-size[1]
    
    newPos=(newPosX, newPosY)
    updatedPositions.append(newPos)

q1=0
q2=0
q3=0
q4=0

print(updatedPositions)
for bot in updatedPositions:
    if(bot[0] < size[0]//2 and bot[1] < size[1]//2):
        q1+=1
    if(bot[0] > size[0]//2 and bot[1] < size[1]//2):
        q2+=1
    if(bot[0] < size[0]//2 and bot[1] > size[1]//2):
        q3+=1
    if(bot[0] > size[0]//2 and bot[1] > size[1]//2):
        q4+=1

print(q1*q2*q3*q4)
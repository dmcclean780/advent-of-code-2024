import re

def is_nearly_integer(num, tolerance=1e-9):
    return abs(num - round(num)) < tolerance

input = open("Day13/input.txt", "r")
input=input.readlines()
machines=[]
machine=[]
for i in input:
    item=list(map(lambda a: re.split(r"[+=]", a)[-1], i.split(':')[-1].strip().split(', ')))
    if item != ['']:
        item[0]=int(item[0])
        item[1]=int(item[1])
        machine.append(item)
    else:
        machines.append(machine)
        machine=[]
machines.append(machine)

total=0
for i in machines:
    prize = i[2]
    buttonA = i[0]
    buttonB = i[1]

    eq1=(buttonA[0], buttonB[0], prize[0])
    eq2=(buttonA[1], buttonB[1], prize[1])

    det = (-1/(eq1[0]*eq2[1]-eq1[1]*eq2[0]))
    inverse=[(eq2[1]*eq1[2]+-eq1[1]*eq2[2]), (-eq2[0]*eq1[2]+eq1[0]*eq2[2])]
    x= det*inverse[0]*-1
    y= det*inverse[1]*-1

    if(is_nearly_integer(x) and is_nearly_integer(y) and x<101 and y<101):
        cost=x*3+y
        total+=cost
        print(cost)

    print(x,y)
    print(buttonA)
    print(buttonB)
    print('\n')

print(total)
import copy
input = open("Day11/input.txt", "r")
input=list(map(lambda a: int(a), input.read().split()))

for j in range(25):
    
    newInput=copy.deepcopy(input)
    splitStones=0

    for i in range(len(input)):
    
        stone=input[i]
        if stone == 0:
            newInput[i+splitStones]=1
        elif len(str(stone))%2==0:
            newInput[i+splitStones]= int(str(stone)[:len(str(stone))//2])
            newInput.insert(i+1+splitStones, int(str(stone)[len(str(stone))//2:]))
            splitStones+=1
        else:
            newInput[i+splitStones]=stone*2024
        

    input=newInput

print(len(input))
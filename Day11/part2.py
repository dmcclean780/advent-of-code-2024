import math
input = open("Day11/input.txt", "r")
input=list(map(lambda a: int(a), input.read().split()))

seenStones={}

def split_number(num):
    num_digits = int(math.log10(num)) + 1
    half_digits = num_digits // 2
    power_of_10 = 10 ** half_digits
    return num // power_of_10, num % power_of_10

def blink(stone, iteration, count):
    if(iteration == 0):
        return count
    if(str(stone) not in seenStones):
        seenStones[str(stone)] = {}
    
    if(iteration not in seenStones[str(stone)]):
        if(isinstance(stone, int)):
            if(stone==0):
              seenStones[str(stone)][iteration] = blink(1,iteration-1, count)
            elif stone >= 10 and (int(math.log10(stone)) + 1) % 2 == 0:
                first_half, second_half = split_number(stone)
                seenStones[str(stone)][iteration]= blink([first_half, second_half], iteration-1, count+1)
            else:
                seenStones[str(stone)][iteration]= blink(stone*2024, iteration-1, count)
        else:
            totalCount=0

            for i in stone:
                thisCount= 1 if isinstance(i, int) else len(i)
                totalCount+=blink(i, iteration, thisCount)
            seenStones[str(stone)][iteration] = totalCount

    return seenStones[str(stone)][iteration]

print(blink(input,75, len(input)))
input = open("Day7/input.txt", "r")
input=input.readlines()
input=list(map(lambda a: a.split(':'), input ))
for i in range(len(input)):
    input[i][0] = int(input[i][0])
    input[i][1] = input[i][1].split()
    input[i][1] = list(map(lambda a: int(a), input[i][1]))

def can_form_target(sequence, target, current=0, index=0):
    if index == len(sequence):
        return current == target
    
    num = sequence[index]
    
    return (can_form_target(sequence, target, current + num, index + 1) or
            can_form_target(sequence, target, current * num if current != 0 else num, index + 1) or
            can_form_target(sequence, target, int(str(current) + str(num)) if current != 0 else num, index + 1))
total=0
for i in range(len(input)):
    result = input[i][0]
    operands = input[i][1]
    total = total + result if can_form_target(operands, result) else total
print(total)
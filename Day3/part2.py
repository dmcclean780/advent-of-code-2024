import re

input = open("Day3/input.txt", "r")
data=input.read()
pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
data = re.findall(pattern, data)
print(data)
sum = 0
enabled=True
for i in range(len(data)):
    if(data[i] == "do()"):
        enabled=True
        continue
    if(data[i] == "don't()"):
        enabled=False
        continue
    else:
        if(enabled):
            print(data[i])
            mul=re.findall("mul\((\d{1,3}),(\d{1,3})\)", data[i])
            numbers = [(int(a), int(b)) for a, b in mul]
            sum += (numbers[0][0]*numbers[0][1])
print(sum)
import re

input = open("Day3/input.txt", "r")
data=input.read()
data = re.findall('mul\(\d{1,3},\d{1,3}\)', data)
print(data)
sum = 0
for i in range(len(data)):
    mul=re.findall("mul\((\d{1,3}),(\d{1,3})\)", data[i])
    numbers = [(int(a), int(b)) for a, b in mul]
    sum += (numbers[0][0]*numbers[0][1])
print(sum)
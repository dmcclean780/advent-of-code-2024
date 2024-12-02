def checkValid(data):
    valid= True
    decreasing = data[0] > data[1]
    for j in range(len(data)-1):
        if(decreasing):
            valid &= data[j] - data[j+1] < 4 and data[j] - data[j+1] > 0
        if(not decreasing):
            valid &= data[j+1] - data[j] < 4 and data[j+1] - data[j] > 0
    return valid


input = open("Day2/input.txt", "r")
list=input.readlines()
data = []
for i in range(len(list)):
    data.append(list[i].strip().split())
    for j in range(len(data[-1])):
        data[-1][j] = int(data[-1][j])

sum = 0
for i in range(len(data)):
    valid = checkValid(data[i])
    if(valid):
        sum+=1
        
print (sum)


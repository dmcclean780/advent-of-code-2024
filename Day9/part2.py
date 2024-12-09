def remove_items(test_list, item): 
  
    # using list comprehension to perform the task 
    res = [i for i in test_list if i != item] 
    return res 

input = open("Day9/input.txt", "r")
input=input.read()
fileCount = len(input)//2
fileID = 0
fileSizes={}
fileLocations={}
blanks=0
totalFileSize=0
for i in range(0,len(input), 1):
    if(i%2 == 0):
        fileSizes[fileID]=int(input[i])
        fileLocations[fileID]=blanks+totalFileSize
        totalFileSize+=int(input[i])
        fileID+=1
    else:
        blanks+=int(input[i])
compressed=[None]*(totalFileSize+blanks)
currentIndex=0
i=0
fileID=0
while i in range(len(compressed)):
    i = fileLocations[fileID]
    for j in range(fileSizes[fileID]):
        compressed[i]=fileID
        i+=1
    fileID+=1
i-=1
while i > -1:
    #print("size"+str(i))
    fileID=compressed[i]
    #print(fileID)
    if(fileID == None):
        i-=1
        continue
    size = fileSizes[fileID]
    for j in range(i):
        space= True
        for k in range(size):
            if(compressed[j+k] != None):
                space = False
                break
        if(space):
            compressed = [None if x == fileID else x for x in compressed]
            for k in range(size):
                compressed[j+k] = fileID
            break
    i-=size



hash=0
for i in range(len(compressed)):
    if(compressed[i]!=None):
        hash+=i*compressed[i]
print(hash)

    

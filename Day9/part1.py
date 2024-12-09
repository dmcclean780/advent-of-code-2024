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
compressed=[None]*totalFileSize
currentIndex=0
i=0
while(i in fileSizes):
    
    if(fileLocations[i] == currentIndex):
        for j in range(fileSizes[i]):
            compressed[currentIndex]=i
            currentIndex+=1
        i+=1
    else:
        lastFile = len(fileSizes)-1
        compressed[currentIndex]=lastFile
        fileSizes[lastFile]-=1
        if(fileSizes[lastFile] == 0):
            fileSizes.pop(lastFile, None)
        currentIndex+=1
    

print(compressed)
hash=0
for i in range(len(compressed)):
    hash+=i*compressed[i]
print(hash)

    

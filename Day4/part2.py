
def checkForWord(i, wordsearch, length):
    cross=""
    if((i-1)%length != length-1 and i>length):
        cross+= wordsearch[i-length-1]
    if((i+1)%length != 0 and i>length):
            cross+= wordsearch[i-length+1] 
    if((i-1)%length != length-1 and (i+length < len(wordsearch))):
           
            cross+=  wordsearch[i+length-1] 
    if((i+1)%length != 0 and (i+length < len(wordsearch))):
          
            cross+= wordsearch[i+length+1]

    s=0
    m=0
    print(cross)
    for j in range(len(cross)):
        if(cross[j]=="M"):
            m+=1  
        if(cross[j]=="S"):
            s+=1
    print(m)
    print(s)
    print("\n")
    if(m==2 and s==2 and len(cross) == 4 and cross[0] != cross[3] and cross[1] != cross[2]):
        return True
    else:
        return False

input = open("Day4/input.txt", "r")
list=input.read()
wordsearch = []
length = 0
while(True):
    if(list[length] != "\n"):
       length+=1
    else:
       break 

wordsearch=list.replace("\n", "")
total = 0
for i in range(len(wordsearch)):
    if(wordsearch[i] == "A"):
        if(checkForWord(i, wordsearch, length)):
            total += 1

print(total)

        

def checkForWord(i, word, length):
    forwards = True
    backwards = True
    up = True
    down = True
    upLeft = True
    downLeft = True
    upRight = True
    downRight = True
    for j in range(1, len(word)):
        # print(len(wordsearch))
        # print(i+j)
        # print((i+j)%length)
        if(forwards and (i+j)%length != 0 and i+j<len(wordsearch)):
            print("right")
            print(wordsearch[i+j])
            forwards &= wordsearch[i+j] == word[j]
        else:
            forwards= False
        if(backwards and (i-j)%length != length-1):
            print("left")
            print(wordsearch[i-j])
            backwards &= wordsearch[i-j] == word[j]
        else:
            backwards= False
        if(up and i>length*(len(word)-1)):
            print("up")
            print(wordsearch[i-(j*length)])
            up &= wordsearch[i-(j*length)] == word[j]
        else:
            up= False
        if(down and (i+length*(len(word)-1)) < len(wordsearch)):
            print("down")
            print(wordsearch[i+(j*length)])
            down &= wordsearch[i+(j*length)] == word[j]
        else:
            down= False
        if(upLeft and (i-j)%length != length-1 and i>length*(len(word)-1)):
            print("up left")
            print(wordsearch[i-(j*length)-j])
            upLeft &= wordsearch[i-(j*length)-j] == word[j]
        else:
            upLeft= False
        if(upRight and (i+j)%length != 0 and i>length*(len(word)-1)):
            print("up right")
            print(wordsearch[i-(j*length)+j])
            upRight &= wordsearch[i-(j*length)+j] == word[j]
        else:
            upRight= False
        if(downLeft and (i-j)%length != length-1 and (i+length*(len(word)-1)) < len(wordsearch)):
            print("down left")
            print(wordsearch[i+(j*length)-j])
            downLeft &= wordsearch[i+(j*length)-j] == word[j]
        else:
            downLeft= False
        if(downRight and (i+j)%length != 0 and (i+length*(len(word)-1)) < len(wordsearch)):
            print("down right")
            print(wordsearch[i+(j*length)+j])
            downRight &= wordsearch[i+(j*length)+j] == word[j]
        else:
            downRight= False

    print("\n\n")
    total=0
    if(forwards):
        total+=1
    if(backwards):
        total+=1
    if(up):
        total+=1
    if(down):
        total+=1
    if(upLeft):
        total+=1
    if(upRight):
        total+=1
    if(downLeft):
        total+=1
    if(downRight):
        total+=1
    return total

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
word="XMAS"
total = 0
x=0
for i in range(len(wordsearch)):
    if(wordsearch[i] == word[0]):
        x+=1
        print(x)
        wordFound = checkForWord(i, word, length)
        total += wordFound

print(total)

        
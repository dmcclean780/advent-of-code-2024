input = open("Day5/input.txt", "r")
list=input.readlines()
rulesParsing = True
rules = []
sequence=[]
for i in range(len(list)):
    if(list[i]=="\n"):
        rulesParsing=False
        continue
    if(rulesParsing):
        rules.append(list[i].strip())
        continue
    if(not rulesParsing):
        sequence.append(list[i].strip())
        continue
ruleIndex={}

for i in range(len(rules)):
    rule = rules[i].split('|')
    if(rule[1] in ruleIndex):
        ruleIndex[rule[1]].append(rule[0])
    else:
        ruleIndex[rule[1]]=[rule[0]]

for i in range(len(sequence)):
    sequence[i]=sequence[i].split(',')

validSequences = []
for i in range(len(sequence)):
    currentValues=[]
    currentSequence = sequence[i]
    validSequence = True
    #print(currentSequence)
    for j in range(len(currentSequence)):
        value = currentSequence[j]
        #print(value)
        #print(ruleIndex[value])
        if (value in ruleIndex):
            requirements = ruleIndex[value]
            valid = True
            for k in range(len(requirements)):
                #print(requirements[k] in currentValues)
                #print(requirements[k] in currentSequence)
                valid &= (requirements[k] in currentValues or requirements[k] not in currentSequence)
            if(valid):
                currentValues.append(value)
            else:
                validSequence = False
        else:
            currentValues.append(value)
        #print(currentValues)
    if(validSequence):
        validSequences.append(currentSequence)

total = 0
for i in range(len(validSequences)):
    middle = ((len(validSequences[i]) - 1)//2)
    print(middle)
    total += int(validSequences[i][middle])

print(total)
from collections import defaultdict, deque

input = open("Day5/input.txt", "r")
input=input.readlines()
rulesParsing = True
rules = []
sequence=[]
for i in range(len(input)):
    if(input[i]=="\n"):
        rulesParsing=False
        continue
    if(rulesParsing):
        rules.append(input[i].strip())
        continue
    if(not rulesParsing):
        sequence.append(input[i].strip())
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

invalidSequences = []
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
    if(not validSequence):
        invalidSequences.append(currentSequence)

# Function to perform topological sort
def topological_sort(items, rules):
    # Step 1: Build the graph
    graph = defaultdict(list)
    in_degree = defaultdict(int)  # Track incoming edges (dependencies)

    # Add edges based on the rules, but only for dependencies in 'items'
    for element, dependencies in rules.items():
        for dep in dependencies:
            if dep in items and element in items:  # Only include dependencies that are in 'items'
                graph[dep].append(element)
                in_degree[element] += 1

    # Initialize the queue with nodes having no dependencies
    queue = deque([item for item in items if in_degree[item] == 0])

    # Step 2: Perform the topological sort
    sorted_order = []
    while queue:
        current = queue.popleft()
        if current in items:  # Only include items in the input list
            sorted_order.append(current)
        # Decrease the in-degree of the neighbors
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 3: Return the sorted order
    return sorted_order

#print(invalidSequences)
fixedSequences=[]
# print(ruleIndex)
# print(invalidSequences[1])
for i in range(len(invalidSequences)):
    sorted_items = topological_sort(invalidSequences[i], ruleIndex)
    invalidSequences[i]= sorted_items
    
   
           
total = 0
for i in range(len(invalidSequences)):
    middle = ((len(invalidSequences[i]) - 1)//2)
    print(middle)
    total += int(invalidSequences[i][middle])

print(total)
input = open("Day1/input.txt", "r")
list=input.readlines()
a = []
b=[]
for i in range(len(list)):
    list[i]=list[i].strip()
    x=list[i].split()
    print(x)
    a.append(int(x[0]))
    b.append(int(x[1]))
#print(a)
#print(b)
total=0
for i in range(len(a)):
    c=min(a)
    a.remove(c)
    d=min(b)
    b.remove(d)
    sum=abs(c-d)
    print(c)
    print(d)
    print(sum)
    print("end")
    total+=sum
print(total)
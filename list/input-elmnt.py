l1=[]

n=int(input("Enter number of elements: "))

for i in range(0,n):
    value=int(input("Enter "+str(i)+"th value: "))
    l1.append(value)
    print(l1)
    
l2=[int(input("Enter "+str(x)+"th value: ")) for x in range(n)]
print(l2)

String1="Hello"

l3=[x for x in String1]
print(l3)

l4=[]
for i in String1:
    l4.append(i)
print(l4)
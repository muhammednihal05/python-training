#Using index of the value
#Index starts from 0

l=[1,2,3,4]

print(l[2]) #Prints 3

l[1]=6 #New list will be [1,6,3,4]
print(l)

print(l[-1]) #Negative indexing starts from the end of the list, l[-1] stands for the last element, l[-2] is the previous one

#l[start:end:incr/decr]

print(l[1:3]) #Prints list from 1st index value to (3-1) index value which is [6,3] here

print(l[:3]) #Stands for l[0:3]

print(l[1:4:2]) #Index incremented by 2 n-1

print(l[3:1:-1]) #Starts from index 3 to 1 in reverse order

print(l[::-1])  #Riverse the list
#deletion of elements from lists

#Can be done in 2 ways

#Using remove function or pop function

#remove(value) removes first occrance of the value from the list.

#pop() removes last element in the list

l=[1,2,3,2]

l.remove(2)

print(l)    #[1,3,2]

l.pop()

print(l)    #[1,3]
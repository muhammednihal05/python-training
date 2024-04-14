#Used to get output

#Syntax: print(value(s), sep= ‘ ‘, end = ‘\n’)

name = "John"
age = 30

a=1
b=2
print("Name:", name, end=", ")
print("Age:", age)
print(a,b,sep=',')

name = "Alice"
age = 25
print("Hello, my name is", name, "and I am", age, "years old.")

print('Hello ' + 'World')

a,b,=10,1000
print('The value of a is {} and b is {}'.format(a,b))
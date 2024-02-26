#Stack implementation using list in python

#Creating a empty list
my_stack = []

#Create push method/function to add values
def push(stack, value):
    stack.append(value)

#Create pop method/function to remove values
def pop(stack):
    return stack.pop()

#print stack before adding values
print(my_stack)

#Adding values into stack
push(my_stack, 2)
push(my_stack, 4)
push(my_stack, 6)

#print after adding values
print(my_stack)

#Remove values
pop(my_stack)

#After pop() print values
print(my_stack)
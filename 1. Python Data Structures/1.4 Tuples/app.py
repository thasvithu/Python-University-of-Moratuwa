import sys

sample = "Vithusan"
print(sample)


my_list = list(sample)
print(my_list)

my_set = set(sample)
print(my_set)

#Creating a Tuple
tuple_1 = ("a", 'b', 20, 5.2)
print(type(tuple_1))

tuple_2 = "a", 'b', 20, 5.2
print(type(tuple_2))
print(tuple_2)

tuple_3 = ("v")
print(type(tuple_3))

tuple_4 = ("v", )
print(type(tuple_4))

#Accessing Values
my_tuple = (15, 20, 69, 32, 17)
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[0:2])

#Nestaed tuple
my_tuple = ((15, 20), (69, 32, 17))
print(my_tuple[0])

#Tuple Packing and Unpacking
#Packing
my_tuple = (2, 4, 6)

#Unpacking
a, b, c = my_tuple
print(a)
print(b)
print(c)


#Insertion, Deletion & Update does not support in tuple


#Check Tuple vs List Memory Consume 
my_list = [15, 20, 69, 32, 17]
my_tuple = (15, 20, 69, 32, 17)

print(sys.getsizeof(my_list))
print(sys.getsizeof(my_tuple))
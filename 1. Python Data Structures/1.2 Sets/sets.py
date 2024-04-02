#Set in python

#Create Set using curly braces
numbers = {2, 4, 8, 10, 12}
print(numbers)
print(type(numbers))


#Create set using Set constructor
numbers1 = set({2, 4, 8, 10, 12})
print(numbers1)
print(type(numbers1))

numbers2 = set([2, 4, 8, 10, 12])
print(numbers2)
print(type(numbers2))

numbers3 = set((2, 4, 8, 10, 12))
print(numbers3)
print(type(numbers3))


# --- SET UNION ---
A = {1, 2, 3, 4, 5}
B = {1, 3, 5, 7, 9}

print(A | B) #A and B
print(A.union(B))


# --- SET INTERSECTION ---
print(A & B)
print(A.intersection(B))


# --- SET DIFFERENCE ---
print(A - B)
print(A.difference(B))

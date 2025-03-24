# Similar to lists , define using ()

tuples = (1 , 2 , 34.5 , 'A_The ')
print(tuples)
print(type(tuples))

# Tuples are immutable
#ex:
# tuples.append(23)
# print(tuples)

#By changing data type tuple to list
tuples = list(tuples)
print(type(tuples))
print(tuples)

# Now you can change it
tuples.append(15787)
print(tuples)

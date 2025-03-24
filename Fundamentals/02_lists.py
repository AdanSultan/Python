# A list can contain different types of variables in it ,
# define as [] brackets.

primeNumber = [2, 3, 5, 7, 11 ]
print(primeNumber)
names = ['Adan ' , 'Ali' , 'Hassan' , 'Umar']
print(names)

newList = primeNumber + names
print(newList)

diffList = ['Adan' , 23 , 14 , 20.9 , " Sultan"]
print(diffList)

# Add more values in List using pre-define functions
primeNumber.append(13)
print(primeNumber)

# Similarly can remove 
names.remove('Umar')
print(names)

# Making List empty using clear

diffList.clear()
print(diffList)

# Can get a specific value by giving its index
print(primeNumber[5])

# Similarly there are many pre-define functions which are in List
# You can learn them by implementing them
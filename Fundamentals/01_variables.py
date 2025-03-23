#Starting.....
rectangleLength = 10
rectangleWidth = 5
rectangleArea = rectangleLength * rectangleWidth
print(rectangleArea)

#Data Types
myAge = 21
print(type(myAge)) # Checking data type

#Print this line
# He said, "Aren't can't shouldn't wouldn't"

# message = "He said,"Aren't can't shouldn't wouldn't""  Giving errors
# print(message) # print it by 2 ways
# use ''' or \ such as:
# By escape character \
message = 'He said, "Aren\'t can\'t shouldn\'t wouldn\'t."'
# By multi line string '''
message1 = '''He said, "Aren't can't shouldn't wouldn't"'''

print(message1)

# Embedding values in Strings
# use %s known as placeholder,
# for values which you want to add later in your strings
#ex:
myAge1 = 21
myName = "Adan"
myMessage = 'My name is %s I am %s years old'
print( myMessage % (myName , myAge1))

# Formated String

name = 'Adan Sultan'
myMess = f"My name is {name} and i am {7*3} years old"
print(myMess)

# Strings most commonly used methods

txt = "Welcome to Uet"
print(txt.upper())
print(txt.lower())
print(txt.__len__())
print(txt.count('o'))
print(txt.replace('o' , 'a'))
print(txt.index('t'))
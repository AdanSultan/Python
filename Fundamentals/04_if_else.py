# Problems Practices
# 01

# age = input("Enter the Age of a Person ")
# age = int(age)
# if(age < 13):
#     print('These are childs')
# elif(age < 20):
#     print('These are Teenagers')
# elif( age < 60 ):
#     print('They are adults ')
# else:
#     print("they are seniors")

# 02

# days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# age = int(input('Enter the age of a person: '))
# day_input = input("Enter the day: ")

# if age > 18 and day_input == "Wednesday":
#     price = 15
#     price -= 2
#     print("You have to Pay $", price)
# elif age < 8 and day_input == "Wednesday":
#     price = 9
#     price -= 2
#     print("You have to Pay $", price)
# else:
#     if age > 18:
#         price = 15
#         print("You have to Pay $", price)
#     elif age < 8:
#         price = 9
#         print("You have to Pay $", price)
        

        #03

# score = int(input("Enter the score of a student "))
# if score >=101:
#         print("Please enter the correct number")
#         exit()
# if (score >= 90 and score <= 100):
#         print("Student will get A Grade")
# elif (score >= 80 and score <= 89):
#         print("Student will get B Grade ")
# elif (score >= 70 and score <= 79):
#         print("Student will get C Grade ")
# elif (score >= 60 and score <= 69):
#         print("Student will get D Grade ")
# else:
#         print("Student Fail")

#04

# color = str(input('Enter the Fruit color '))

# if color == 'Yellow':
#         print('Ripe the fruit')
# elif color == 'Green':
#         print('Do not ripe the fruit')
# else:
#         print("Any other color , brown the fruit is overripe")

#05

# weather = str(input("Enter the weather situation "))
# if weather == "Sunny":
#         print("Go for a walk")
# elif weather == "Rainy":
#         print("Read the book")
# elif weather == "Snowy":
#         print("Built a snowman")
# else:
#      print("Tell me the weather conditions which i write in above"

#06

passwordChecker = input("Enter the length of a password ")

if len(passwordChecker) <=6 :
    print('Your Password is week choose the strongest password')
elif 7<= len(passwordChecker) <=10:
        print("Your Password is medium")
elif len(passwordChecker) >=11:
        print("Your password is strong")
else:
        print("Enter the length of Password")
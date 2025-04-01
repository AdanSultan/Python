# For loop
# for x in range(0 , 5):
#     print(f"Adan {x}")

# names = ['Ali' , 'Sultan' , 'Adan']
# for x in names:
#     print(x)

#Given List: [1 , 2, -3 , -5, -7 , 8 , 12, 15, 29, 40]
#Tell me how many numbers are negative in it

# numbers = [1 , 2, -3 , -5, -7 , 8 , 12, -15, 29, -40]
# negative_count_number = 0
# for num in numbers:
#     if num < 0:
#         print(num)
#         negative_count_number +=1
# print('Total negative numbers are :' , negative_count_number)


# Sum of odd number which you written

# n = int(input("Enter a number: "))
# sum=0
# for num in range(0,n+1):
#     if(num%2!=0):
#         sum+=num
# print("Sum of Odd numbers from 0 to",n,"is",sum)

#Multiplication table for a given number

# n = int(input('Enter a number : '))
# for i in range(1,11):
#     if i==5:
#         continue
#     print(f'{n} * {i}  = ',n * i )

# Factorial of a number

# n = int(input('Enter a number : '))
# factorial = 1
# while n > 0:
#     factorial = factorial * n
#     n = n-1
# print('factorial of a number is : ', factorial)

#

# while True:
#     n = int(input('Enter a number : '))
#     if 1<= n <= 10:
#         print('Thanks.......')
#         break
#     else:
#         print('Invalid number, try again')




import time

attempt = 0
maximum_retries = 5
wait_time = 1

while attempt < maximum_retries:
    print('Attempts : ', attempt + 1 , '-- wait time : ', wait_time)
    time.sleep(wait_time)
    wait_time *=2
    attempt +=1

    #General Applying Pre define functions
# names.append('Kanwar')
# print(names)
# names.insert(2 , 'ali')
# print(names)
# names.__len__()
# print(names)
# names.remove('ali')
# print(names)


# Table: 1
# print('---------------------------')
# y = 1
# x = 1
# z = x * y
# for z in range(1 , 11):
#     print(f'{x} * {y} = ', z )
#     y = y+1
# print('---------------------------')

#Table:2

# print('---------------------------')
# y = 1
# for y in range(1 , 11):
#     x = 2
#     z = x * y
#     print(f'{x} * {y} = ', z )
#     y = y + 1
# print('---------------------------')

#Table:3

# print('---------------------------')
# y = 1
# for y in range(1 , 11):
#     x = 3
#     z = x * y
#     print(f'{x} * {y}  =', z )
#     y = y + 1
# print('---------------------------')


#Best.......
# for i in range(1,13):
#     for x in range(1,13):
#         print(f'{i} * {x}  =  {i * x}')
#     print('--------------------')




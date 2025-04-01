# Basic function:

# def square(n):
#     return n**2
# print(square(4))

# ^ bitwise xor operator:
# a = 4^2
# print(a)  # output : 6

# Take 2 numbers as a parameters which return their sum

# def sum(a,b):
#     return a+b
# print(sum(5,6))

# def mul(c,d):
#     return c*d
# print(mul(6 , 'h' ))

# import math
# def circle(radius):
#     area = math.pi * radius ** 2
#     circumference = 2 * math.pi * radius
#     return area , circumference

# a , c = circle(4)
# print(f'Area :  {a:.2f} Circumference :  {c:.2f}' )


# write a function that takes variable number of arguments and returns their sum


# def sum_all(*args):
#     return sum(args) 
# print(sum_all(1,2))
# print(sum_all(1,2,3))
# print(sum_all(1,2,3,4))

# def min_value(*args):
#     print(args)
#     return min(args)
# print(min_value(4,5))


# function with kwargs

# def print_kwargs(**kwargs):
#     for key , value in kwargs.items():
#         print(f'{key} : {value}')
    
# print_kwargs(name = 'Adan' , department = 'CS')
# print_kwargs(name = 'Hassan' , department = 'EE' , city = 'Lahore')
# print_kwargs(name = 'Ali', department = 'SE')


# Generator function with yield 

# Hint 

# 1. return Keyword:

# Purpose: The return keyword is used to return a value from a function and terminate the function's execution.
# Behavior: Once a return statement is executed, the function stops running, and the value is returned to the caller.
# Use Case: Use return when you want to return a single value or a collection (e.g., list, tuple) and terminate the function.


# yield Keyword:

# Purpose: The yield keyword is used to create a generator function. It allows the function to "pause" its execution and return a value to the caller, but it can resume execution from where it left off.
# Behavior: When yield is used, the function becomes a generator. It does not terminate after yielding a value; instead, it can continue execution when the generator is iterated.
# Use Case: Use yield when you want to produce a sequence of values lazily (one at a time) instead of returning them all at once.



# def odd_generator(limit):
#     for i in range(1 , limit + 1, 2):
#         yield i

# for num in odd_generator(10):
#     print(num)


# recursive function simple / factorial


def factorial(n ):
    if n == 0:
        return 1
    else:
        return n  * factorial(n-1)
print(factorial(3))


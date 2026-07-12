# 1. What is a function in Python, and why is it useful?
# a function in python is called as block of reusable code that performs specific task 
# instead of writing the same code multiple times , we use function
# it reduces the code to simpler way 

# 2. Differentiate between positional, keyword, default, and variable-length arguments.
# positional argument -- values are passed in the same order of the function 
# keyword argument --  values are passed using parameter names . it is irrespective of order
# default -- you will assign some dafault value in the function itself . so that when you dont pass any value it uses the dafault value 
# variable length parameters -- when you dont know how many arguments you will pass ,you will use *args for positional arguments and *kwargs for keyword arguments 

# 3. What happens if a function does not have a return statement?
# if a function does not have return statement it will automatically returns NONE 

# 4. Explain local vs global variables in the context of functions.
#           Local Variable	                                             Global Variable
# A variable declared inside a function.	                    A variable declared outside all functions.
# It can be used only inside that function.	                    It can be used throughout the program.
# It exists only while the function is executing.	            It exists until the program ends.

# 5. What is recursion, and when should it be used?
# recursion is a programming technique in which a function calls itself . 
# it compulsory needs base case to stop running 
# it is used to calculate smaller problems like factorual calculations and fibonacci series , etc 


def sum_digits(n):
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10

    return total

num = int(input("Enter a number: "))
print("Sum of digits:", sum_digits(num))

def is_palinddrome(n):
    if n == n[::-1]:
        return "It is a palindrome"
    else:
        return "It is not a palindrome"
txt = input("Enter a string: ")
print(is_palinddrome(txt))


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter a number: "))
print("Factorial:", factorial(num))


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime number")
else:
    print("Not a prime number")
    
    
#Write a lambda function to square a number.
square = lambda x: x * x
num = int(input("Enter a number: "))
print("Square:", square(num))

# 2. Demonstrate map, filter, and reduce with simple examples.
# map -- applies a function to all the items in the list and returns a new list with the results
# filter -- filters the items in the list based on a condition and returns a new list with the items that satisfy the condition
# reduce -- applies a function to the items in the list and returns a single value

# A closure is a function that remembers the variables from its outer function, even after the outer function has finished executing.
def outer():
    x = 10

    def inner():
        print(x)

    return inner

result = outer()
result()

for x in range(97,123):
    print(chr(x),end=" ")

for x in range(32,127):
    print(chr(x),"=",x)

num= int(input("enter your number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)

n = int(input("enter your number:"))
for i in range(n,0,-1):
    print(i)


num = int(input("enter your digit:"))
sum = 0
while num > 0:
    digit=num%10
    sum = sum + digit
    num = num//10
print("sum of digits=",sum)

n = int(input("enter your number:"))
sum = 0
for i in range(2,n+1,2):
    sum = sum + i
print("sum of even numbers=",sum)

n = int(input("enter your number:"))
sum = 0
for i in range(1,n+2,2):
    sum = sum + i 
print("sum of odd numbers=",sum)



num= input("enter your number:")
if len(num)==1:
    print("swapped number=",num)
else:
    swapped = num[-1] + num[1:-1] + num[0]
    print("swapped number=",swapped)


num = (input("enter your number:"))
first= int(num[0])
last = int(num[-1])
sum = first + last
print("sum of first and last digit=",sum)


num = int(input("enter your number:"))
product = 1
while num>0:
    digit = num % 10
    product = product * digit
    num = num//10
print("product of digits=",product)


num = int(input("Enter a number:"))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number =", reverse)

num = int(input("Enter a number: "))

reverse = 0

for i in range(len(str(num))):
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number =", reverse)



base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = 1
count = 1

while count <= exponent:
    result = result * base
    count = count + 1

print("Power =", result)

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = 1

for i in range(exponent):
    result = result * base

print("Power =", result)



num = int(input("enter your number:"))
fact = 1 
for i in range(1,num + 1):
    fact  = fact * i
print("factorial of number=",fact)


num = int(input("Enter a number: "))

temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** 3
    temp = temp // 10

if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


n = int(input("Enter the value of n: "))

for num in range(1, n + 1):
    temp = num
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** 3
        temp = temp // 10

    if sum == num:
        print(num)
        

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal

print("Amount =", amount)
print("Compound Interest =", compound_interest)


num = int(input("Enter a number: "))

i = 2
flag = 0

while i < num:
    if num % i == 0:
        flag = 1
        break
    i = i + 1

if num <= 1:
    print(num, "is not a prime number")
elif flag == 0:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

num = int(input("Enter a number: "))

flag = 0

for i in range(2, num):
    if num % i == 0:
        flag = 1
        break

if num <= 1:
    print(num, "is not a prime number")
elif flag == 0:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")



num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print(original, "is a palindrome number")
else:
    print(original, "is not a palindrome number")

num = input("Enter a number: ")

for digit in num:
    if digit == '0':
        print("Zero", end=" ")
    elif digit == '1':
        print("One", end=" ")
    elif digit == '2':
        print("Two", end=" ")
    elif digit == '3':
        print("Three", end=" ")
    elif digit == '4':
        print("Four", end=" ")
    elif digit == '5':
        print("Five", end=" ")
    elif digit == '6':
        print("Six", end=" ")
    elif digit == '7':
        print("Seven", end=" ")
    elif digit == '8':
        print("Eight", end=" ")
    elif digit == '9':
        print("Nine", end=" ")



num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

hcf = 1

for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i

print("HCF =", hcf)


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

lcm = max(num1, num2)

while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        break
    lcm = lcm + 1

print("LCM =", lcm)

print("---------------------------------------------------------------------------------------------")






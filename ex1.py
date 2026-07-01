# convert the string "1010" into integer base 2
str1="1010"
print(str1)
print(int(str1,2))

# consider an items into the cart, remove some items and print remaining items
cart=["keyboard","mouse","laptop","cpu"]
print(cart)
del cart[3]
print(cart)

#consider a list of elements,marks of a student,sum,average,grading
marks=[50,75,87,68,95]
print(marks)
total=sum(marks)
print(total)

average=total/5
print(average)

if average >=90:
   print("A+")
elif average >=80:
     print("A")
elif average >=70:
     print("B")
elif average >=60:
     print("C")
elif average >=50:
     print("D")
else:
     print("E")

#write a program to accept a number from the user print whether it is a positive or negative number
number = int(input("enter your number:"))
if number >0:
   print("positive number")
else:
     print("Negative number")

#write a program to know whether a number is divisible of 2 
number = int(input("enter your number:"))
if number % 2 ==0:
   print("divisible")
else:
    print("non divisible")

#write a program to know the number is greater than 10
number = int(input("enter your number:"))
if number > 10:
   print("greater than 10")
else:
    print("less than 10")

# write a program to check whether a year is leap year or not an leap year
year = int(input("enter your year:"))
if (year % 4 == 0 and year % 100!= 0) or (year % 100 == 0 and year % 400 == 0):
   print("is a leap year")
else:
    print("is not a leap year")







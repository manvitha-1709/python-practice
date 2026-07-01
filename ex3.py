number1 = float(input("enter your number:"))
number2 = float(input("enter your number:"))
if number1>number2:
   print("maximum number=",number1)
else:
    print("maximum number=",number2)


num1 = float(input("enter your number:"))
num2 = float(input("enter your number:"))
num3 = float(input("enter your number:"))
if num1>num2 and num1>num3:
   print("maximum num=",num1)
elif num2>num1 and num2>num3:
   print("maximum num=",num2)
else:
     print("maximum num=",num3)


num = int(input("enter your number:"))
if num>0:
    print("number is positive")
elif num<0:
      print("number is negative")
else:
     print("number is zero")


num = int(input("enter your number:"))
if num % 5 == 0 and num % 11 == 0 :
    print("number is divisible by both 5 and 11")
else:
    print("number is not divisible by 5 and 11")


num = int(input("enter your number:"))
if num%2 == 0:
    print("number is even")
else:
    print("number is odd")


char= input("enter your character:")
if ('a'<= char <='z') or ('A'<= char <='Z'):
    print("your character is an alphabet")
else:
    print("your character is not an alphabet")
    

char= input("enter your character:")
if char in ['a','e','i','o','u'] or char in ['A','E','I','O','U']:
   print("your character is an vowel")
else:
   print("your character is an consonant")


char= input("enter your character:")
if ('a'<= char <= 'z') or ('A'<= char <= 'Z'):
    print("your character is an alphabet")
elif ('0'<=char<='9'):
    print("your character is an digit")
else:
    print("your character is an special character")


char= input("enter your character:")
if ('a'<=char<='z'):
   print("your character is an lower case alphabet")
else:
   print("your character is an upper case alphabet")


month=int(input("enter your month number:"))
if month==1:
   print("31")
elif month == 2:
     print("28")
elif month ==3:
     print("31")
elif month==4:
     print("30")
elif month ==5:
     print("31")
elif month==6:
     print("30")
elif month ==7:
     print("31")
elif month == 8:
     print("31")
elif month==9:
     print("30")
elif month==10:
     print("31")
elif month==11:
     print("30")
else:
     print("31")


week=int(input("enter your week number:"))
if week==1:
   print("sunday")
elif week == 2 :
     print("monday")
elif week == 3:
     print("tuesday")
elif week == 4 :
     print("wednesday")
elif week ==5 :
     print("thursday")
elif week ==6:
     print("friday")
else:
     print("saturday")


amount=int(input("enter your amount:"))

notes500= amount//500
amount%= 500

notes200=amount//200
amount%=200

notes100= amount//100
amount%=100

notes50 = amount//50
amount%=50

notes20 = amount//20
amount%=20

notes10 = amount//10
amount%=10

notes5 = amount//5
amount%=5

notes2 = amount//2
amount%=2

notes1 = amount

total_notes = (notes500 + notes200 + notes100 + notes50 + notes20 + notes10 + notes5 + notes2 + notes1)
print("total number of notes=",total_notes)



a = int(input("enter first angle:"))
b = int(input("enter second angle:"))
c = int(input("enter third angle:"))
if (a>0 and b>0 and c>0) and (a+b+c==180):
    print("triangle is vaild")
else:
    print("triangle is invalid")



a = int(input("enter first side:"))
b = int(input("enter second side:"))
c = int(input("enter third side:"))
if (a+b>c and a+c>b and b+c>a):
    print("triangle is valid")
else:
    print("triangle is invalid")



a = int(input("enter first side:"))
b = int(input("enter second side:"))
c = int(input("enter third side:"))
if (a == b == c):
    print("triangle is equivalent")
elif (a==b!=c or a==c!=b or b==c!=a):
    print("triangle is isosceles")
else:
    print("triangle is scalene")


sp= float(input("enter selling price:"))
cp= float(input("enter cost price:"))
if sp > cp:
    profit= sp - cp
    print("profit=",profit)
elif cp > sp:
    loss = cp - sp
    print("loss=",loss)
else:
    print("no profit no loss")


physics=float(input("enter your physics marks:"))
chemistry=float(input("enter your chemistry marks:"))
biology=float(input("enter your biology marks:"))
mathematics=float(input("enter your mathematics marks:"))
computer=float(input("enter your computer marks:"))

total_marks = (physics + chemistry + biology + mathematics + computer)
percentage = (total_marks / 500 * 100)

print(total_marks)
print(percentage)

if percentage >=90:
   print("Grade A")
elif percentage >= 80:
     print("Grade B")
elif percentage >=70:
     print("Grade C")
elif percentage >= 60:
     print("Grade D")
elif percentage >=50 :
     print("Grade E")
else:
     print("Grade F")



basic_salary = float(input("enter basic salary:"))
if basic_salary<=10000:
    hra= basic_salary * 20/100
    da = basic_salary * 80/100
elif basic_salary <=20000:
     hra= basic_salary * 25/100
     da = basic_salary * 90/100
else:
     basic_salary >20000
     hra= basic_salary * 30/100
     da = basic_salary * 95/100

gross_salary= (basic_salary + hra + da )

print("gross salary=",gross_salary)       

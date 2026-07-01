rows = int(input("enter your rows:"))
for i in range(1,rows +1):
    num=1
    for j in range(1,i+1):
        print(num,end=" ")
        num+=2
    print()


num = int(input("enter your number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)


x=[10,20,30,40,50]
for i in x:
    if i == 30:
        break
    print(i)

print("----------------------------")

x = [10,20,30,40,50]
for i in x :
    if i==30:
        continue
    print(i)


x = 30
if x==30:
    pass
else:
    pass
print("none")


rows = int(input("Enter the number of rows: "))

i = 1

while i <= rows:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1

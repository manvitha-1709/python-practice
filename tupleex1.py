tuple1= (1, 2, 3, 4, 5)
print("the third element of tuple1 is:", tuple1[2])

tuple2= (1,)
print(tuple2)
print(type(tuple2))

tuple3 = (12,12,12,13,14,15,15)
number = int(input("enter the number to count:"))
count = tuple3.count(number)
print("the", number, "is repeated", count, "times in the tuple3")

tuple4 = (1, 2, 3, 4, 5)
print("the index of 3 in tuple4 is:",tuple4.index(3))

tuple5 = (10,20,30,40,50)
print(tuple5[1:4])

tuple6 = (1, 2, 3, 4, 5)
tuple7 = (6, 7, 8, 9, 10)
tuple8 = tuple6 + tuple7
print("the concatenated tuple is:",tuple8)

print(tuple1*3)

num = int(input("enter the number to check:"))
if num in tuple8:
    print(num, "is present in the tuple8")
else:
    print(num, "is not present in the tuple8")

list = list(tuple1)
list.append(6)
tuple1 = tuple(list)
print(tuple1)

tuple9 = ((1, 2), (3, 4), (5, 6))
print(tuple9[1][1])

tuple10 = (12, 34, 56, 78, 90)
print("the maximum value in tuple10 is:", max(tuple10))
print("the minimum value in tuple10 is:", min(tuple10))

tuple11 = (5 , 2 , 9 , 1 , 7)
print(sorted(tuple11))

tuple8 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("the sum of tuple8 is:",sum(tuple8))
print("the average of tuple8 is", sum(tuple8)/len(tuple8))

student = ("Manvitha", 17, "CSE")
name, age, branch = student
print("Name:", name)
print("Age:", age)
print("Branch:", branch)

# tuple packing and unpacking:
# tuple packing is the process of creating a tuple by grouping multiple values together into a single entity.
# tuple unpacking is the process of extracting the individual values from a tuple and assigning them to separate variables.

t = ("apple", "banana", "cherry","kiwi","mango")
longest = t[0]
for i in t:
    if len(i) > len(longest):
        longest = i
print("the longest string in the tuple is:",longest)

tuple12 = (1,2,3,4,2,1,4,5,6,7,8,9,10)
result = []
for i in tuple12:
    if i not in result:
        result.append(i)
print("tuple after removing duplicates:", tuple(result)) 

tuple13 = ("ram","arav","krishna","prasanna","benni","sathesh,","pamba")
sorted_tuple = sorted(tuple13)
print("the sorted tuple is:",tuple(sorted_tuple))

t1 = (1, 2, 3, 4, 5)
t2 = (6, 7, 8, 9, 10)
print("tuple before swapping:", t1, t2)
t1, t2 = t2, t1
print("tuple after swapping:", t1, t2)


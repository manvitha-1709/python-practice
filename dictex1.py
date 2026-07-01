#dictionary 
#write a program to create a phonebookusing dictionary in python
phonebook={
    "teja":'9848126352',
    "sonu":'9550432220'


}
phonebook["yoshi"]='9876543210'
name=input("enter name to search:")
if name in phonebook:
    print(f"{name}'s phone number is {phonebook[name]}")
else:
    print(f"{name} is not found in the phonebook.")
#student marks using dictionary
student_marks={
    "student1":85,
    "student2":90,
    "student3":78,
    'student4':92
}
student_name=input("enter student name to check marks:")
if student_name in student_marks:
    if student_marks[student_name] > 90:
        print("student has scored above 90,grade A")
    elif student_marks[student_name] > 80:
        print("student has scored above 80,grade B")
    else:
        print("student has scored below 80,grade C")
else:
    print(f"{student_name} is not found in the student marks.")
#write a program to merge two dictionaries in python
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
res=dict1.copy()
for key, value in dict2.items():
    res[key] = value
print("Merged dictionary:", res)

#dictionary comprehension
#write a program to create a dictionary which contains the squares of numbers from 1 to 5 using dictionary comprehension
#1:1,2:4,3:9,4:16,5:25
squares={ x:x*x for x in range(1,6)}
print(squares)
#use cases:
##write a program to convert a list of tuples into a dictionary using dictionary comprehension
studentslist=[('teja',85),('sonu',90),('yoshi',78)]
print(dict(studentslist))
#list to dictionary using dictionary comprehension
list1=['a','b','c','d']
#a=1,b-2,c=3,d=4
#packing and unpacking in tuple
#packing:it is the process of combining multiple values into a single variable, usually a tuple.
fruits=('apple','banana','cherry')
#unpacking:it is the process of extracting individual values from a packed variable, such as a tuple, and assigning them to separate variables.
fruit1,fruit2,fruit3=fruits
print(fruit1)
print(fruit2)
print(fruit3)
#* variable-length argument unpacking:it allows you to unpack an arbitrary number of values from a tuple or list into separate variables using the * operator.
fruits_list=['apple','banana','cherry','date']
fruit1,fruit2,*other_fruits=fruits_list
print(fruit1)
print(fruit2)
print(other_fruits)





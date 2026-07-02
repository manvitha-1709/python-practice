dict1 = {
    "student name": "manvitha",
    "age": 17,
    "grade": "A"
}
print(dict1)

dict2 = {"name":"manvitha","city":"hyderabad","salary":50000}
print(dict2["city"])
dict2["country"]="india"
print(dict2)
dict2["salary"]=60000
print(dict2)

dict1.pop("age")
print(dict1)

if "email" in dict1:
    print("Email is present in the dictionary")
else:
    print("Email is not present in the dictionary")

print("total key-value pairs in the dictionary:",len(dict2))

for i in dict2.keys():
    print(i)
for i in dict2.values():
    print(i)

for i in dict2:
    print(i,":",dict2[i])

sum = 0
for value in dict2.values():
    if type(value) == int:
        sum += value
print("the sum of all integer values in the dictionary is:",sum)

dict3 = {"a": 1, "b": 2, "c": 3}
print(max(dict3.values()))
print(min(dict3.values()))

s = input("enter a string:")
freq = {}
for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print("the frequency of each character in the string is:",freq)

s = input("enter a string:")
words = s.split()
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
print(word_freq)

dict4 = {"x": 5, "y": 2, "z": 8, "w": 1}
print(dict3.update(dict4))
print(dict3)

squares = {x:x*x for x in range(1,11)}
print(squares)

squares = {x:x*x for x in range(1,21) if x%2==0}
print(squares)

swapped = {}
for key in dict2:
    swapped[dict2[key]] = key
print(swapped)

for values in sorted(dict2):
    print(values, ":", dict2[values])
for keys in sorted(dict2):
    print(keys, ":", dict2[keys])

students = {
    "student1": {
        "name": "manvitha",
        "age": 17,
        "marks": 95
    },
    "student2": {
        "name":"bindu",
        "age": 18,
        "marks": 96
    },
    "student3":{
        "name":"lokhya",
        "age": 19,
        "marks": 92
    }
}
print(students)
print(students["student2"]["marks"])
students["student3"]["age"]= 20
print(students)

d = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}

freq = {}

for value in d.values():
    if value in freq:
        freq[value] += 1
    else:
        freq[value] = 1

for key in d:
    if freq[d[key]] > 1:
        print(key)
    
new_dict = {}
for key in d:
    if d[key] not in new_dict.values():
        new_dict[key] = d[key]
print(new_dict)


keys = ["name","age","city"]
values = ["manvitha",17,"hyderabad"]
students = {}
for i in range(len(keys)):
    students[keys[i]] = values[i]
print(students)


d1 = {
    "name": "Manvitha",
    "age": 17,
    "grade": "A"
}

d2 = {
    "age": 18,
    "grade": "B",
    "city": "Hyderabad"
}

for key in d1:
    if key in d2:
        print(key)


students = {
    "Manvitha": 85,
    "Rahul": 70,
    "Priya": 92,
    "Kiran": 68
}

for name in students:
    if students[name] > 75:
        print(name)

cart = {
    "Apple": 2,
    "Milk": 1,
    "Bread": 3
}

cart["Eggs"] = 12

cart["Milk"] = 2

del cart["Bread"]

print(cart)

print("Total items in cart:", len(cart))
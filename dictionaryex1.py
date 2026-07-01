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









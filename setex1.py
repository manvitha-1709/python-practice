# difference between set and list
# set:
# -- it is an unordered collection of elements
# -- it is mutable
# -- it does not allow duplicate elements
# -- it is defined using curly braces {} or set()
# -- indexing and slicing are not supported
# list:
# -- it is an ordered collection of elements
# -- it is mutable
# -- it allows duplicate elements
# -- it is defined using square brackets [] or list()
# -- indexing and slicing are supported

set1 = {1, 2, 3, 4, 5, 5, 2}
print(set1)

set1.add(6)
print(set1)
set1.remove(5)
print(set1)

print(5 in set1)

set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))
print(set1 | set2)

print(set1.intersection(set2))
print(set1 & set2)

print(set1.difference(set2))
print(set1 - set2)

print(set1.symmetric_difference(set2))
print(set1 ^ set2)

list1 = [1, 2, 3, 4, 5, 5, 2]
set3 = set(list1)
print(set3)

list2 = [1,2,3,1,2,3,4,5,6,7]
result = []
for num in list2:
    if list2.count(num) == 1:
        result.append(num)
print("the number of unique elements in the list is:", len(result))

set3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set4 = {5, 6, 7, 8, 9,}
print(set4.issubset(set3))
print(set4.isdisjoint(set3))

list3=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list4=[5, 6, 7, 8, 9]
common = set(list3) & set(list4)
print("the common elements are:",common)

set5 = {'a','e','i','o','u','A','E','I','O','U'}
char = input("enter a character:")
if char in set5:
    print("the character is a vowel")
else:
    print("the character is a consonant")

set6 = {1,2,3,4,5,6,7,8,9,10}
set6.difference_update({5,6,7,8,9})
print(set6)

str = "helloworld"
set7 = set(str)
print("the set of unique characters in string is:",set7)

set6 = {1,2,3,4,5,6,7,8,9,10}
longest =max(set6)
smallest = min(set6)
print("the longest element in the set is:",longest)
print("the smallest element in the set is:",smallest)

set7 = set(map(int,input("enter the elements of the first set:").split()))
set8 = set(map(int,input("enter the elements of the second set:").split()))
print(set7|set8)
print(set7&set8)
print(set7-set8)
print(set7^set8)

sentence = "defeat the defeat before it defeats you"
unique_words = set(sentence.split())
print("the unique words in the sentence are:",unique_words)

s = "python programming is fun"
unique_chars = set(s)
for ch in unique_chars:
    print(ch ,":",s.count(ch))



# n = int(input("enter number of elements in list:"))
# numbers = []
# for i in range(n):
#     num = int(input("enter number:"))
#     numbers.append(num)
# print("The list of numbers is:", numbers)

# largest = numbers[0]
# for num in numbers:
#     if num>largest:
#         largest = num
# print("The largest number in the list is:", largest)

# n = int(input("enter number of elements in a list:"))
# numbers = []
# for i in range(n):
#     num = int(input("enter number:"))
#     numbers.append(num)
#     largest = second_largest = float('-inf')
#     for num in numbers:
#         if num>largest:
#             second_largest = largest
#             largest = num
#         elif num>second_largest and num!=largest:
#             second_largest = num
# print("the second largest number is :",second_largest)


# n = int(input("enter number of elements in a list:"))
# numbers = []
# for i in range(n):
#     num = int(input("enter number:"))
#     numbers.append(num)
#     smallest =numbers[0]
#     for num in numbers:
#         if num<smallest:
#             smallest = num
# print("the smallest number is :",smallest)


# list1 = [1,3,5,2,4,3,7,9,3,6]
# print(list1.count(3))

# n= int(input("enter number of elements in a list:"))
# numbers = []
# for i in range(n):
#     num = int(input("enter number:"))
#     numbers.append(num)
# x = int(input("enter number to count:"))
# count = 0
# for num in numbers:
#     if num == x:
#         count += 1
# print(f"The number {x} appears {count} times in the list.") 

# n = int(input("enter number of elements in a list:"))
# numbers = [] 
# for i in range(n):
#     num = int(input("enter number:"))
#     numbers.append(num)
# x= int(input("enter number to remove:"))
# while x in numbers:
#         numbers.remove(x)
# print("Updated list:", numbers)


# n = int(input("enter number of elements in a list:"))
# numbers = []
# for i in range(n):
#     num = int(input("enter number:"))
#     numbers.append(num)
# reversed_list = []
# for i in range(len(numbers)-1, -1, -1):
#     reversed_list.append(numbers[i])
# print("Reversed list:", reversed_list)


# list1 = [2,8,5,0,4,1,6,9]
# list1.sort()
# print(list1)

# # check whether a list is sorted in ascending order or not 
# n = int(input("enter number of elements in a list:"))
# numbers = []
# for i in range(n):
#     num = int(input("enter number:"))
#     numbers.append(num)
# is_sorted = True
# for i in range(len(numbers)-1):
#     if numbers[i] > numbers[i+1]:
#         is_sorted = False
#         break
# if is_sorted:    
#     print("The list is sorted in ascending order.")
# else:   
#     print("The list is not sorted in ascending order.")             

# n = int(input("enter number of elements in a list:"))
# numbers = []
# for i in range(n):
#     num = int(input("enter number:"))
#     numbers.append(num)
# total = sum(numbers)
# print("the sum of the numbers in the list is:",total)

# n = int(input("enter number of elements in a list:"))
# numbers = []
# for i in range(n):
#     num = int(input("enter number:"))
#     numbers.append(num)
# average = sum(numbers)/len(numbers)
# print("average of the numbers in the list is:",average)

# list1 = [1,2,3,4,5,6,7,8,9,0,]
# new_list = []
# for num in list1:
#     if num % 2 == 0:
#         new_list.append(num)
# print("The even numbers in the list are:", new_list)

# # find the index of an targeting element without using index() method
# n = int(input("enter number of elements in a list:"))
# numbers = []
# for i in range(n):
#     num = int(input("enter number:"))
#     numbers.append(num)
# target = int(input("enter the target number to find its index:"))
# index = -1
# for i in range(len(numbers)):
#     if numbers[i] == target:
#         index = i
#         break
# if index != -1:
#     print(f"The index of {target} in the list is: {index}")
# else:
#     print(f"{target} is not found in the list.")


# n = int(input("enter number of elements in a list:"))
# numbers = []
# for i in range(n):
#     num = int(input("enter number:"))
#     numbers.append(num)
# positive = 0
# negative = 0
# zero = 0
# for num in numbers:
#     if num > 0:
#         positive+=1
#     elif num <0:
#         negative+=1
#     else:
#         zero+=1
# print(f"the number of positive numbers in the list is: {positive}")
# print(f"the number of negative numbers in the list is: {negative}")
# print(f"the number of zeros in the list is: {zero}")


# n = int(input("Enter number of elements: "))

# numbers = []

# for i in range(n):
#     num = int(input("Enter element: "))
#     numbers.append(num)

# duplicates = []

# for num in numbers:
#     if numbers.count(num) > 1 and num not in duplicates:
#         duplicates.append(num)

# print("Duplicate elements:", duplicates)

# lst = [1,3,2,4,5,3,1,]
# for i in lst:
#     if lst.count(i)==1:
#         print("first non repeating element is:",i)
#         break
# else:
#     print("no non repeating element found")
        

# lst = list(map(int,input("enter the numbers separated by space:").split()))
# for i in lst:
#     if lst.count(i)==1:
#         print("first non repeating element is:",i)
#         break
# else:
#     print("no non repeating element found")


# lst = list(map(int,input("enter the numbers separated by space:").split()))
# visited = []
# for i in lst:
#     if i not in visited:
#         print(i,"appears",lst.count(i),"times in the list")
#         visited.append(i)

# list1 = list(map(int,input("enter elements of first list:").split()))
# list2 = list(map(int,input("enter elements of second list:").split()))
# if sorted(list1) == sorted(list2):
#     print("The two lists are equal.")
# else:
#     print("The two lists are not equal.")

# n = int(input("enter the value of n:"))
# lst = list(map(int,input("enter the numbers :").split()))
# total = n*(n+1)//2
# actual = sum(lst)
# missing_number = total - actual
# print("the missing number is :",missing_number)

# lst = list(map(int,input("enter the numbers separated by space:").split()))
# max_freq = 0
# most_frequent = lst[0]
# for i in lst:
#     if lst.count(i) > max_freq:
#         max_freq = lst.count(i)
#         most_frequent = i
# print("the most frequent element in the list is:",most_frequent)

# list1 = [1,2,3,4,5,6,7,8,9]
# if 2 in list1:
#     print("2 is present in the list.")
# else:    
#     print("2 is not present in the list.")

# lst = list(map(int,input("enter the numbers separated by space:").split()))
# target = int(input("enter the target number to find:"))
# if target in lst:
#     print("the number is present in list")
# else:
#     print("the number is not present in list")

# lst = list(map(int,input("enter the numbers separated by space:").split()))
# temp = []
# for num in lst:
#     if lst.count(num)==1:
#         temp.append(num)
# print("the single time occurence elements are:", temp)

# lst1 = [1,2,3,4,5]
# lst2 = [4,5,6,7,8]
# merged = lst1 + lst2
# result = []
# for num in merged:
#     if num not in result:
#         result.append(num)
# print("the merged list without duplicates is:",result)


# lst= list(map(int,input("enter list elements:").split()))
# k = int(input("enter number of positions to rotate:"))
# k = k%len(lst)
# rotated = lst[-k:] + lst[:-k]
# print("rotated list:",rotated)

# lst = list(map(int,input("enter list elements:").split()))
# k = int(input("enter number of positions to rotate:"))
# k = k % len(lst)
# rotated = lst[k:] + lst[:k]
# print("rotated list:", rotated)

# lst = list(map(int,input("enter list elements:").split()))
# n = int(input("enter chunk size:"))
# for i in range(0, len(lst), n):
#     print(lst[i:i+n])

# list1 = [1,2,3,4,5]
# list1[0], list1[-1] = list1[-1], list1[0]
# print("swapped list:",list1)

# lst = [1,0,2,0,3,0,4,5,0]
# result = []
# for i in lst:
#     if i!= 0:
#         result.append(i)
# zero_count = lst.count(0)
# for i in range(zero_count):
#     result.append(0)
# print("list after moving zeros to the end:",result)


# list1 = [1,2,3,4,1,2,3,5,6,7,8]
# result = []
# for i in list1:
#     if i not in result:
#         result.append(i)
# print("list after removing duplicates:",result)


# lst = [10,20,30,40,50]
# n = int(input("enter the element to insert:"))
# for i in range(len(lst)):
#     if n <lst[i]:
#         lst.insert(i,n)
#         break
# else:
#     lst.append(n)
# print("list after inserting the element:",lst)






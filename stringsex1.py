# char = input("enter your string:")
# if char==char[::-1]:
#     print("string is palindrome")
# else:
#     print("string is not palindrome")
    
# string = input("enter your string:")
# vowels = 0
# consonants = 0
# for ch in string:
#     if ch.isalpha():
#         if ch.lower() in 'aeiou':
#             vowels += 1
#         else:
#             consonants += 1
# print("number of vowels :", vowels)
# print("number of consonants :", consonants)


# string = input("enter your string :")
# result = ""
# for char in string:
#     if char not in result:
#         result = result + char
# print("after removing duplicates :",result)



# str1 = input("enter your string1:")
# str2 = input("enter your string2:")
# if sorted(str1) == sorted(str2):
#     print("the strings are anagrams")
# else:
#     print("the strings are not anagrams")



# string = input("enter your string:")
# freq = {}
# for char in string:
#     if char in freq:
#         freq[char] = freq[char] + 1
#     else:
#         freq[char]=1
# print("frequency of characters in the string:")
# for char in freq:
#     print(char,":",freq[char])


# str = input("enter your string:")
# rst = ""
# for char in str:
#     rst=char + rst
# print("reversed string is:",rst)    

# str = input("enter your string:")
# words_list = str.split()
# print("number of words in the string:",len(words_list))
# max=0
# maxword="" 
# for word in words_list:
#     if len(word)>max:
#         max=len(word)
#         maxword=word
# print("the longest word in the string is:",maxword) 


# str = input("enter your string:")
# words = str.split()
# result = []
# for char in words:
#     result = result + [char[::-1]]
# print("the reversed words in the string are:",result)

# # resverse the order of words in the string
# str = input("enter your string:")
# words = str.split()
# result = []
# for char in words:
#     result = [char] + result
# print("the reversed order of words in the string are:",result)
#explanation: In this code, we take a string input from the user and split it into words using the split() method. We then create an empty list called result to store the reversed order of words. We iterate through each word in the words list and add it to the beginning of the result list using list concatenation. Finally, we print the reversed order of words in the string.


# # # find the logest substring without repeating characters
# # str = input("enter your string:")
# # max_length = 0
# # start = 0
# # char_index = {}
# # for i, char in enumerate(str):
# #     if char in char_index and char_index[char] >= start:
# #         start = char_index[char] + 1
# #     char_index[char] = i
# #     max_length = max(max_length, i - start + 1)
# # print("the length of the longest substring without repeating characters is:", max_length)

# # #find the longest palindromic substring in a given string
# # str = input("enter your string:")
# # def longest_palindromic_substring(s):
# #     n = len(s)
# #     if n == 0:
# #         return ""
    
# #     start, end = 0, 0
    
# #     for i in range(n):
# #         len1 = expand_around_center(s, i, i)      # Odd length palindrome
# #         len2 = expand_around_center(s, i, i + 1)  # Even length palindrome
# #         max_len = max(len1, len2)
        
# #         if max_len > (end - start):
# #             start = i - (max_len - 1) // 2
# #             end = i + max_len // 2
            
# #     return s[start:end + 1]

# # def expand_around_center(s, left, right):
# #     while left >= 0 and right < len(s) and s[left] == s[right]:
# #         left -= 1
# #         right += 1
# #     return right - left - 1









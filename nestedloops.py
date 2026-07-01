# # #nested loops:if loop inside another loop
# # #1
# # #1 2
# # #1 2 3
# # for i in range(1,4):
# #     for j in range(1,i+1):
# #         print('*',end=" ") #print(j,end=" ")
# #     print()

# # #1
# # #2 2
# # #3 3 3
# # #4 4 4 4
# # for i in range(1,5):
# #     for j in range(1,i+1):
# #         print(i,end=" ")
# #     print()
# # #1
# # #2 3
# # #4 5 6
# # #7 8 9 10
# # num = 1
# # for i in range(1,5):
# #     for j in range(1,i+1):
# #         print(num,end=" ")
# #         num += 1
# #     print()
# # #match case:
# # #it is a new feature introduced in Python 3.10 that allows you 
# # # to perform pattern matching on values, similar to switch statements in other programming languages.

# # day = "sunday"
# # match day:
# #     case "monday":
# #         print("it is the first day of the week")
# #     case "tuesday":
# #         print("it is the second day of the week")
# #     case "wednesday":
# #         print("it is the third day of the week")
# #     case "thursday":
# #         print("it is the fourth day of the week")
# #     case "friday":
# #         print("it is the fifth day of the week")
# #     case "saturday":
# #         print("it is the sixth day of the week")
# #     case "sunday":
# #         print("it is the seventh day of the week")
# #     case _:
# #         print("invalid day")

# # month=5
# # day=15
# # match month:
# #     case "january":
# #         print("it is the first month of the year")
# #         print("it is week day ", day)
# #     case "february":
# #         print("it is the second month of the year")
# #     case "march":
# #         print("it is the third month of the year")
# #         print("it is week day ", day)
# #     case "april":
# #         print("it is the fourth month of the year")
# #     case "may":
# #         print("it is the fifth month of the year")
# #     case _:
# #         print("invalid month")
# from unittest import case


# month=input("enter month:")
# days=int(input("enter days:"))
# match month:
#     case  "january" | "march" | "may" | "july" | "august" | "october" | "december":
#         print(f'{month} has 31 days')
#     case "february":
#         if days == 29:
#             print(f'{month} has 29 days')
#         else:
#             print(f'{month} has 28 days')
#     case "april" | "june" | "september" | "november":
#         print(f'{month} has 30 days')
#     case _:
#         print("invalid month")


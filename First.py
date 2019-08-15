# a = input()
# a = a.split(" ")
# for i in a[::-1]:
#     print(i, end=" ")

# a = input()
# b = list()
# for i in a:
#     b.append(i)
# if b == b[::-1]:
#     print("Yes")
# else:
#     print("No")

# a = input()
# b = list()
# for i in a:
#     b.append(i)
# x = len(b)
# for i in range(len(b)):
#     x -= 1
#     if b[i] != b[x]:
#         print("No")
#         break
# if i == len(b)-1:
#     print("Yes")

# a = int(input())
# b = int(input())
# d = 0
# for i in range(a, b+1, 1):
#     if i % 4 == 0:
#         if i % 100 != 0:
#             c = 366
#         else:
#             c = 365
#     if i % 400 == 0:
#         c = 366
#     else:
#         c = 365
#     d = c + d
# print(d)

# a = int(input())
# b = int(input())
# d = 0
# while a <= b:
#     if a % 4 == 0:
#         if a % 100 != 0:
#             c = 366
#         else:
#             c = 365
#     if a % 400 == 0:
#         c = 366
#     else:
#         c = 365
#     a += 1
#     d = c + d
# print(d)

# a = input()
# a = a.split()
# k = 0
# for i in a:
#     k = int(i) + k
# print(k)
#
# a = int(input())
# a = a // 5
# b = a + (a // 7)
# print(b)

# def a(b):
#     b = b // 5
#     c = b + (b // 7)
#     return c
# dog = int(input("Enter >> "))
# print(a(dog))

# a = input()
# b = input()
# a = a.split(":")
# b = b.split(":")
# t1 = [int(c) for c in a]
# t2 = [int(d) for d in b]
# if t1[0] > t2[0]:
#     time1 = ((12 - t1[0]) * 60) - t1[1]
# else:
#     time1 = (t1[0] * 60) + t1[1]
#
# time2 = (t2[0] * 60) + t2[1]
# print(time1, time2)
# if t1[0] > t2[0]:
#     time = (time1 + time2) // 60
#     sec = (time1 + time2) % 60
# else:
#     time = (time2 - time1) // 60
#     sec = (time2 - time1) % 60
# print(time, ":", sec)
#
# a = input()
# a = a.split(" ")
# a = [int(i) for i in a]
# print(a[0]+a[1])
#
# n = int(input("Enter n > "))
# i = 1
# a = 0
# while i <= n:
#     a = a + i
#     i += 2
# print(a)

# a = int(input())
# i = 3
# c = list()
# for i in range(3, 10000000):
#     g = False
#     for j in range(2, i):
#         if i % j == 0:
#             g = True
#     if g == False:
#         print(i)

# n = int(input())
# x = 1
# i = 2
# while x < n:
#     c = False
#     i += 1
#     for j in range(2, i):
#         if i % j == 0:
#             c = True
#     if c == False:
#         x += 1
# print(i)

# a = int(input())
# for i in range(1, a+1):
#     print(i, end=" ")
#     for j in range(2, a+1):
#         print(j*i, end=" ")
#     print(" ")

# a = int(input())
# for i in range(1, a+1):
#     print(i, end=" ")
#     for j in range(1, a+1):
#

# a = input()
# a = a.split(",")
# b = [int(i) for i in a]
# print(b)
# x = True
# c = b[0]
# i = 1
# for i in range(1, len(b)):
#     if c < (b[i]):
#         x = True
#     else:
#         x = False
#     print(c, b[i])
#     c = b[i]
# if x == False:
#     print("yes")
# else:
#     print("no")

# a = input()
# x = 0
# y = 0
# for i in a:
#     if i == "(":
#         x += 1
#     if i == ")":
#         x -= 1
#     if i == "[":
#         y += 1
#     if i == "]":
#         y -= 1
# if x == 0 and y == 0:
#     print("yes")
# else:
#     print("no")

# a = int(input())
# b = list()
# c = list()
# for i in range(a):
#     n = 0
#     b = input()
#     b = b.split(" ")
#     if b[0] == "donate":
#         c.append(b[1])
#         d = [int(i) for i in c]
#     if b[0] == "report":
#         for j in range(len(d)):
#             n += d[j]
#         print(n)

# a = input()
# a = a.split("-")
# startday = 2
# b = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# c = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
# d = [int(i) for i in a]
# j = 0
# k = 0
# while k < 12:
#     j = 0
#     while j < b[k]:
#         if startday == 7:
#             startday = 1
#         else:
#             startday += 1
#         j += 1
#         if j == d[0] and k == d[1]-1:
#             print(c[startday-1])
#             break
#     k += 1

# n = int(input())
# num = []
# while True:
#     print(n)
#     num.append(n % 2)
#     n = n // 2
#     if n <= 0:
#         break
# print(num)
# i = 0
# b = len(num)
# print()
# for i in range(len(num)):
#     print(num[i], end="")






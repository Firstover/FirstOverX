# Problem A
# a = input()
# # a = a.split()
# # a = [int(i) for i in a]
# # print(a[0]+a[1])

# Problem B
# n = int(input())
# temp = 0
# for i in range(1, n+1,2):
#     temp = i + temp
# print(temp)

# Problem J
# n = int(input())
# num = []
# while True:
#     num.append(n % 2)
#     n = n // 2
#     if n <= 0:
#         break
# print(num)
# i = 0
# b = len(num)
# m = []
# x = 0
# for i in range(len(num)):
#     m.append(num[i])
#     x += 1
#     if x == 4:
#         x = 0
# print(x)
# for j in range(4-x):
#     m.append(0)
# d = 0
# for k in m[::-1]:
#     print(k, end="")
#     d += 1
#     if d == 4:
#         d = 0
#         print(end=" ")

# a = input()
# a = a.split()
# b = 1
# c = []
#
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(i+1)
#     b += 1
# del c[len(c)-1]
# for j in c:
#     print(j, end="")

# a = int(input())
# print(a)
# for i in range(1, a+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("z", end=" ")
#     elif i % 5 == 0:
#         print("y", end=" ")
#     elif i % 3 == 0:
#         print("x", end=" ")
#     else:
#         print(i, end=" ")

# startday = int(input())
# b = int(input())
# i = 0
# c = 0
# while i < b:
#     if startday == 7:
#         startday = 1
#     else:
#         startday += 1
#     i += 1
#     if startday == 1:
#         c += 1
#     if startday == 7:
#         c += 1
# print(c)


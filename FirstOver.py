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

# n = int(input())
# m1 = [[0 for i in range(n)] for i in range (n)]
# m2 = [[0 for i in range(n)] for i in range (n)]
# for i in range(n):
#     a = input()
#     a = a.split(" ")
#     a = [int(i) for i in a]
#     for j in range(len(a)):
#         m1[i][j] = a[j]
# r = n
# c = n
# s = True
# for k in range(len(m1)):
#     c = n
#     r -= 1
#     for f in range(len(m1)):
#         c -= 1
#         m2[r][c] = m1[k][f]
#         if m1[k][f] < 0:
#             s = False
# if m1 == m2 and s == True:
#     print("Symmetric")
# elif m1 == m2 and s == False:
#     print("Non-Symmetric")
# else:
#     print("Non-Symmetric")

# a = list()
# a.append([0, 1])
# a.append([1, 1])
# print(a)
# a.insert(1, [2, 2])
# print(a)
# a.pop(0)
# print(a)

# n = int(input())
# p = list()
# c = True
# for i in range(3, n+1):
#     c = True
#     for j in range(3, i, 2):
#         print(i, j)
#         if i % j == 0 or i % 2 == 0:
#             c = True
#         else:
#             c = False
#     if c == False:
#         p.append(j)
# print(p)

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

# n = input()
# n = n.split()
# n = [int(i) for i in n]
# temp = 0
# count = 0
# count2 = 0
# for i in range(len(n)):
#     for j in range(i+1, len(n)): 
#         if n[i] > n[j]:
#             temp = n[i]
#             n[i] = n[j]
#             n[j] = temp
#             count += 1
#         count2 += 1
# print(count, count2)
# print("%d %d" %(n[0],n[(len(n)-1)]))



    
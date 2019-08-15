# min = 3
# max = int(input())
# a = list()
# if max > 6:
#     for num in range(min, max + 1):
#         if num > 1:
#             for v in range(2, num):
#                 if (num % v) == 0:
#                     break
#             else:
#                 a.append(num)

#     b = list()
#     for i in range(len(a)):
#         for j in range(len(a)):
#             if a[i] + a[j] == max:
#                 b.append([a[i], a[j]])
#     c = 0
#     d = 0
#     for k in range(len(b)):
#         if b[k][1] > d:
#             d = b[k][1]
#             c = b[k][0]
#         else:
#             d = d
#             c = c

#     print(c, d)
#     if len(b) == 0:
#         print("Goldbach")
#     else:
#         print("%d = %d + %d" % (max, c, d))
# else:
#     print("Err")

n = int(input())
shop = input()
shop = shop.split()
shop = [int(i) for i in shop]
c = int(input())
money = list()
for i in range(c):
    money.append(int(input()))
for j in range(len(money)):
    count = 0
    for k in range(len(shop)):
        if shop[k] <= money[j]:
            count += 1
    print(count)
# # 100以内的素数：
# number = 2
# while number <= 100:
#     i = 2
#     if_prime = True
#     while i < number:
#         if number % i == 0:
#             if_prime = False
#             break
#         i = i + 1
#     if if_prime:
#         print(number)
#     number += 1
from unittest import result

# data2 = [[1, -290, 3, 4], [5, 67, -7, 89],[9,10,11,112]]
# #1 2 3 4
# #5 6 7 8
# #9 10 11 12
# print(data2)
# print(len(data2[0]))
# print(data2[2][3])
# # 找出二维数组里的最大值
# maxvalue = data2[0][0]
# r = 0#行
# c = 1#列
# while r < len(data2):
#     c = 0
#     while c < len(data2[r]):
#         if data2[r][c] > maxvalue:
#             maxvalue = data2[r][c]
#             c += 1
#     r += 1
# print(maxvalue)

# #切片 （左闭右开）
data = [100,27,33,46,56,90,7,8,9]
# result = data[1:8]
# print(result)
# #拿出4，6，8
# result_1 = data[3:8:2]
# print(result_1)
# #从小到大排序
# data.sort()
# print(data)
# #从大到小排序
# data.sort(reverse=True)
# print(data)

result = 100 in data
print(result)
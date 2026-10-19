data = (1,2,3,4,5,6,7,8,9)
print(type(data))
print(len(data))
data_1 = (1,2,[3,4,5,6,7],8,9)
print(len(data_1))
data_1[2][3]= 10
print(data_1)
index = 0
while index < len(data_1):
    print(id(data_1[index]))
    index += 1
index = 0
data_1[2][2] = 12
while index < len(data_1):
    print(id(data_1[index]))
    index += 1
# 集合 // 无序，没有重复值的列表
data = {2,100,79,56,45}
print(type(data))
print(data)
print(100 in data)
print(len(data))
# 增删
data.add(12)
print(data)
data.remove(12)
print(data)
# 交集 并集 减法
data_2 = {2,78,79,90,12}
# 交集
print(data.intersection(data_2))
# 并集
print(data.union(data_2))
# 减法
print(data.difference(data_2))
data = [1,[2,3,4],{24,89,70},'TOHKA',{'shixiang':102}]
# 遍历
for i in data[4]:
    print(i)    # 输出键
    print(data[4][i])   # 输出值
# 同时输出键和值
# .items我会键值对一个一个放到元组里面去
for i in data[4].items():
    print(i)
# 只想拿到里面的值
for i in data[4].values():
    print(i)
# 输出0到100
for d in range(1,101):
    print(d)
# 输出单数
for d in range(1,101,2):
    print(d)
# 输出位置和数据
# enumerate(枚举)
for d in enumerate(data):
    print(d)
# 分别输出位置和数据
for index,d in enumerate(data):
    print(index)
    print(d)
# 往一个列表里添加1到100的整数
data_1 = [number for number in range(1,101)]
print(data_1)
data_2 = []
for e in range(1,101):
    data_2.append(e)
print(data_2)
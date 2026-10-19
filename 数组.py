# 数组（python里面叫列表）[]里可填数据，用，隔开
# 下标和索引（相当于列表里的序号）从0开始的，带负号只是相反顺序
shuzulianxi = ['T','T','O']
print(shuzulianxi) #打印出list,包含所有数据
print(type(shuzulianxi))  # 类型为Lift
print(shuzulianxi[1]) # 指定某一位置的数据
print(shuzulianxi[-1]) # 只是顺序的不同，要注意倒数是从1开始，正数是从0开始
(shuzulianxi[0]) = 'TOHKA' #更改数据，相当于‘赋值’
print(shuzulianxi)
shuzulianxi.append('H') # 尾部补入数据,这里面的小数点表示隶属关系
print(shuzulianxi)
shuzulianxi.insert(4,'K') # 插入数据(索引，内容)
print(shuzulianxi)
# del shuzulianxi[4] / shuzulianxi.pop(),括号里不填东西，默认是删除最后面的
shuzulianxi.pop(0)
print(shuzulianxi)
shuzulianxi.remove('O') # remove是根据list里的数据直接删除，使用的前提是数据要真实存在
print(shuzulianxi)

# 找出列表里的最小值 (遍历列表)
data = [25,7,21,8,4,2,0,-23523,624,26]
minvalue = data[0] # 目前的最小值
i = 1 # 循环的次数
# len():可自动获取列表的长度
while i < len(data):
    if data[i] < minvalue:
        minvalue = data[i] # 替换成最新最小值
    i += 1
print(minvalue)

data_1 = [1,2,'TOHKA',[3,4,5]]
print(data_1)
print(len(data_1))
print(data_1[3])
print(data_1[3][2])
print(len(data_1[3]))


# 字符串
# 字符串和列表很相像
data = 'TO HKA'
print(data)
# 列表
print(data[0])
print(data[-1])
print(len(data))
# 切片
print(data[0:2])
# 字符串不能随便修改
data.find('TOHKA')
print(data.find('TOHKA'))
print(data[0:])
print(data.split(' '))
# 字符串可以做加法和乘法
data_1 = '你' + '干' + '嘛'
print(data_1)
data_2 = '鸡哥' * 5
print(data_2)
# 格式化字符串    本质是填空
name = "TOHKA"
yue = 4
rizi = 10
# 1.占位符式子：%d(整数)，%f(小数)，%s(字符串)
shixiang = '你好%s,您的生日是%d月%d号'% (name,yue,rizi)
print(shixiang)
# 2.format式：
shixiang = '你好{},您的生日是{}月{}号'.format(name,yue,rizi)
print(shixiang)
# 3.f-string式：
shixiang = f'你好{name},您的生日是{yue}月{rizi}号'
print(shixiang)
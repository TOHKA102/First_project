# 类（对象的模板）  对象
# __init__(self):表示重构函数
# self表示隶属关系
class people:
  def __init__(self,name,age,sex):
      self.name = name
      print(name)
      print(age)
      print(sex)
  def xihuanshiwu(self,string):
      print(string)

  def suki(self,string):
      print(string)

# 一个对象一个点应该是可以访问类里面的数据的
# 如果你想要这个类有自己的属性，self+.
yedaoshenshixiang = people('夜刀神十香',20,'女')
yedaoshenshixiang.xihuanshiwu('黄豆粉面包')
yedaoshenshixiang.suki('五河士道')
print(yedaoshenshixiang.name)
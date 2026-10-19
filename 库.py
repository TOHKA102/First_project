import os.path
print(os.path.abspath('./'))

from random import shuffle, choice
data = ['shixiang','qinli','kuangsan','sixinai','meijiu']
shuffle(data)
print(data)
print(choice(data))
# from operator import add
#
#
# def add(number1,number2=3):
#     return number1 + number2,number1,number2
# result,a,b = add(3)
# print(result,a,b)

def add(a:int,b:int=3)->int:
    return a+b
result = add(3)
print(result)
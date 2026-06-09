import math
def divide(str):
    mid = math.ceil(len(str)/2)
    a = str[:mid]
    b = str[mid:]
    return a,b
def mangle(a,b):
    a_1,a_2 = divide(a)
    b_1,b_2 = divide(b)
    return a_1+b_1+a_2+b_2

print(mangle("kimokono","abcde"))

import sys

print type(sys.maxsize)
#<type 'int'>
print type(sys.maxsize+1)


def fun1(x, y=9):
    a = x * y
    return "string" + str(a)

print(fun1(1))

f = lambda x, y : x * y

print(f(2,3))

l = [1,2,3,4,5]
print(map(lambda x: x * 2, l))
print(reduce(lambda x, y: x + y, l))

print(filter(lambda  x : x > 2 , l))













l = [1,2,3,4]

# return *2
def fun1(in_list):
    l = []
    for i in in_list:
        l.append(i * 2)
    return l

out = fun1(l)
print(out)

print(map(lambda x: x * 2, l))
print(reduce(lambda x, y: x + y, l))


print( str(1) + "hi")
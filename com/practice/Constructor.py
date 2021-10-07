
# __init__ is private or a magic method. It usually call automatically when new instance constructed, user no need to call it.
# If it is not present, it is not called
# The self argument is the first appearance of the instance
# we can assign the attribute values before we can create the instance.

class Myclass(object):
    c = 9
    def __init__(self, value):
        try:
            self.val = int(value)
        except ValueError:
            self.val = 0

    def increment(self):
        self.val = self.val +1




obj = Myclass("hi")


obj.increment()
obj.increment()
print obj.val
print obj.c


obj1 = Myclass(2345)

obj1.increment()
obj1.increment()
obj1.increment()
obj1.increment()

print obj1.val

class sample:
    pass


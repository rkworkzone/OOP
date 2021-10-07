# Attributes and variables in the class are accessible through the instance
# Instance attributes are also accessible by instance
# when we us the object.attribute syntax to look up the attribute, It will check first in the instance then in the class
# attribute look up order is instance first then  class
class MyClass(object):
    classy = "This is a classy attribute"
    def set_value(self):
        self.insty = "This is a insty attribute"


obj = MyClass()
obj.set_value()
#print obj.insty
#print obj.classy

obj1 = MyClass()
#print obj1.insty
#print obj1.classy

class YClass(object):
    classy = "class value"

yobj = YClass()
print yobj.classy

yobj.classy = "changed to instance value"
print yobj.classy

del yobj.classy

print yobj.classy

#del yobj.classy
print pow(2,33*222222)
print yobj.classy

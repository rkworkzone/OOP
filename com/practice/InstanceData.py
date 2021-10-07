class InstanceCounter(object):
    count = 0

    def __init__(self,value):
        self.val = value
        InstanceCounter.count += 1

    def set_val(self,newValue):
        self.val = newValue

    def get_value(self):
        return self.val

    def get_count(self):
        return InstanceCounter.count

a = InstanceCounter(4)
b = InstanceCounter(5)
c = InstanceCounter(9)
d = InstanceCounter(43)

for obj in (a,b,c,d):
    print "Instance attribute ", obj.val
    print "Class attribute" , InstanceCounter.count
    print "Class attribute calling yia instance/ object" , obj.count


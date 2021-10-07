import random

import os,sys,datetime,string,time,collections,re,calendar

import yaml,json, csv, datetime

k=time.time()

class MyClass(object):
    var = 10
    def myMethod(self):
       self.va = random.randrange(2,5)
        #return "I am in my method. testing the method"


class my_class2():
    c = 2342534254
    def add(self, i , j):
        return i + j



o = my_class2()

print o.add(2,3)


that_obj = MyClass()
that_obj.myMethod()
print that_obj.va
print(that_obj.__setattr__("va",15))
print that_obj.va

l = time.time()


print l-k

#print that_obj.__init__

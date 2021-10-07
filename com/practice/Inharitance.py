
class Date(object):
    def get_date(self):
        return "2016-06-15"

class Time(Date):
    def get_time(self):
        return "12:55:00"


dt = Date()
tm = Time()

print tm.get_date()
print tm.get_time()


class Animal(object):
    def __init__(self,name):
        print self
        print type(self)
        self.name = name

    def doSomething(self):
        print "Do some thing"


class Dog(Animal):
    def sound(self):
        return "bo0000000"

class GermanDog(Dog):
    def special(self):
        return "tail is so long"


def nano(self):
    return "nano tech"


print nano()



gd = GermanDog("jaggu")
print gd.special()
print gd.sound()
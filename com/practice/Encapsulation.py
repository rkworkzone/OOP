class MyClass(object):
    def set_val(self, value):
        try:
            self.val = int(value)
        except ValueError:
            return
        self.val = value

    def get_val(self):
        return self.val

    def increment_val(self):
        self.val = self.val + 1


myObj = MyClass()
myObj.set_val(20)
print myObj.get_val()

myObj.set_val("ramaknath ileni")
#myObj.val = "chandra"
print myObj.increment_val()

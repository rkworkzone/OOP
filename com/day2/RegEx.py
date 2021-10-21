import re


print(dir(re))

c = re.compile(r'^This\s.*\d$')

x = re.search(c, "This is Rama44")
print(x.group())
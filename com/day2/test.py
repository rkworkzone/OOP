import yaml
import json
y = yaml.load(file("../../conf/config.yaml"))
print type(y)

print y
# with open("../../conf/sample.json") as f:
#     data = json.load(f)
#
# print data
# print data['widget']['debug']


file = open("../../conf/config.yaml")
for line in file :
    print line.strip()
file.close


with open("../../conf/config.yaml") as f:
    for l in f:
        print  l.strip()


s = "Thi is sample write"
f = open("../../data/sample.txt", 'a')
f.write(s+'\n')
f.close()

import sys
import json
list = []
output = []
lookup = {"element": "Element()",
          "class": "print('Its a class for ' + temp[1])"}


def Element():
    object = {}
    object['tag'] = temp[1]
    props = json.loads(temp[2])
    for x in props:
        object[x] = props[x]
    output.append(object)


for i in sys.argv:
    list.append(i)
f = open(list[1], "r")
for x in f:
    y = str(x).replace("\n", "")
    temp = y.split(" ", 2)
    exec(lookup[temp[0]])
r = open("output.txt", "w")
r.write(str(output))
r.close()

from operator import xor
import sys
import json
list = []
output = []
lookup = {"element": "Element()",
          "class": "Class()",
          "nest": "Nest()"}
classes = {}
nests = {}


def Element():
    object = {}
    object['tag'] = temp[1]
    if temp[1] in classes:
        for x in classes[temp[1]]:
            object[x] = classes[temp[1]][x]
    props = json.loads(temp[2])
    for x in props:
        if x == "nest":
            if props[x] in nests:
                object[x] = nests[props[x]]
        if x == "label":
            print("tomik")
            label = {}
            label['tag'] = "label"
            label['for'] = props['id']
            label['innerHTML'] = props[x]
            if "label" in classes:
                for x in classes['label']:
                    label[x] = classes['label'][x]
            output.append(label)
        else:
            object[x] = props[x]
    output.append(object)


def Class():
    newclass = {}
    props = json.loads(temp[2])
    for x in props:
        newclass[x] = props[x]
    classes[temp[1]] = newclass


def RenderNestElement(tempnest):
    object = {}
    object['tag'] = tempnest[1]
    if tempnest[1] in classes:
        for x in classes[tempnest[1]]:
            object[x] = classes[tempnest[1]][x]
    props = json.loads(tempnest[2])
    for x in props:
        object[x] = props[x]
    return object


def Nest():
    newnest = []
    elements_in_nest = temp[2].split(' -- ')
    for x in elements_in_nest:
        tempnest = x.split(" ", 2)
        if not tempnest[0] in lookup:
            print("Error: Non-existent statement in Nest.")
            quit()
        newnest.append(RenderNestElement(tempnest))
    nests[temp[1]] = newnest


for i in sys.argv:
    list.append(i)
f = open(list[1], "r", encoding="utf-8")
for x in f:
    y = str(x).replace("\n", "")
    temp = y.split(" ", 2)
    if not temp[0] in lookup:
        print("Error: Non-existent statement.")
        quit()
    exec(lookup[temp[0]])
r = open("output.txt", "r+", encoding="utf-8")
r.write("")
raw = str(output)
cooked = raw.replace("'", '"')
r.write(cooked)
print("OK")
r.close()

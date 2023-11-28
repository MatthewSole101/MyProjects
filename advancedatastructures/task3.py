





d1 = {1, 2, 3, 4, 5, 6}
d2 = {1, 2, 3, 4, 5, 6}
oldlist = {}
newlist = {}
for i in d1:
    for x in d2:
        newtuple = d1 + d2
        oldlist[x] = newtuple
        newlist[x] = newtuple + oldlist



for i in newlist:
    print(newlist[i])
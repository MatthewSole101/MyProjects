def list_to_dict():
    count = 0
    while listlength != count:
        dic[count] = list1[count]
        dic[count] = list2[count]
        count = count + 1
    else:
        print(dic)



dic = {}
list2 = []
list1 = []



inp = int(input("Write a integer: "))
list1.append(inp)

while inp != 00:
    inp = int(input("Write another integer or stop by typing '0': "))
    list1.append(inp)
else:
    list1.pop(-1)

inp = input('Write a letter: ')
list2.append(inp)


while inp != '.':
    inp = input("Write another letter or stop by typing '0': ")
    list2.append(inp)
else:
    list2.pop(-1)




listlength = len(list1)

list_to_dict()
def next_ints():
    count = 0

    while count != length:
        num = list[count]
        num = num - 1
        newlist.append(num)
        count = count + 1
    else:
        newlist.f
        print(newlist)

list = []
num = 0
newlist = []



inp = int(input("Write a integer: "))
list.append(inp)

while inp != 00:
    inp = int(input("Write another integer or stop by typing '0': "))
    list.append(inp)

else:
    list.pop(-1)

length = len(list)


next_ints()

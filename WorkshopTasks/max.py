def hello(max = 0):
    list = []
    end = False
    last = list[-1:]
    add = ''


    while end == False:
        if last == "end":
            end == True
        else:
            add = input("Write a number or write end: ")
            list.append(add)
    else:
        list.sort()
        print('The highest value is', list[-2:])

    return list[-2:]


hello(max=0)

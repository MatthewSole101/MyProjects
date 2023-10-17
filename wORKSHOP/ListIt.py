months = ['January', 'March', 'May' , 'September', 'December']

inp = input('Write a day of the month: ')

exist = months.count(inp)

length = len(months)

while length != 11:
    if exist == 0:
        months.append(inp)
    elif exist >0:
        print('IDK')
else:
    months.pop(2)
    months.pop(3)
    months.pop('October')

print(months)



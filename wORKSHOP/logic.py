x = int(input('Write a n integer: '))
y = int(input('Write another integer: '))
z = int(input('Write another integer: '))

one = False
two = False
three = False

if x < y or y>z:
    one = True
    print('1.', one)
else:
    print('1.', one)

if y!=z:
    two = True
    print('2.', two)
else:
    print('2.', two)

if x >= z or y>z and x!=y:
    three = True
    print('3.', three)
else:
    print('3.', three)
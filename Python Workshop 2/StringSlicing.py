inp = input('Write a string: ')

length = len(inp)

num = length - 3

print('The first three letters are: ', inp[:3])
print('The last three letters are: ', inp[num:])
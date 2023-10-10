s1 = input('Enter a string: ')
s2 = input('Enter another string: ')

s1l = len(s1)
s2l = len(s2)




s1f = s1[s1l-1:]
s2f = s2[s2l-1:]

s1new = s1.replace(s1[s1l-1:], s2f)

s2new = s2.replace(s2[s2l-1:], s1f)

print(s2new, s1new)
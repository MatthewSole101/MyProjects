
def checkPrime(num):
    if num == 2:
        print(num, 'is a prime number')
        primelist.append(num)
    for i in range(2, num):
        if num % i == 0:
            break
        else:
            print(num, 'is a prime number')
            primelist.append(num)
            break

list = []
primelist = []
#length of list
count = 0
count2 = 0
total = 0
count3 = 0
length = 0
mean = 0
isPrime = False
inp = int(input("Write a integer: "))
list.append(inp)

while inp != 00:
    inp = int(input("Write another integer or stop by typing '0': "))
    list.append(inp)
    count = count + 1


else:

    list.pop(-1)
    length = len(list)
    list.sort()


while count != count2:
    total = total + list[count2]
    count2 = count2 + 1



else:
    print('The sum is', total)

# if list[count3] > 1:
#
#     for count3 in range(2, int(list[count3]/2)+1):
#         if (list[count3] % count3) == 0:
#             print(list[count3], "is NOT a prime number")
#     else:
#         print(list[count3], "is a prime number")
#         primelist.append(list[count3])
# else:
#     print(list[count3], 'is not a prime number')

# for count3 in range(2, int(list[count3] / 2) + 1):
#     if list[count3] <= 1:
#         print(list[count3], 'is not a prime number')
#     if list[count3] == 2:
#         print(list[count3], 'is a prime number')
#         primelist.append(list[count3])
#     if list[count3] % count3 == 0:
#         print(list[count3], 'is not a prime number')
#     else:
#         print(list[count3], 'is not a prime number')
#         primelist.append(list[count3])

while length != count3:
    prime = list[count3]
    checkPrime(prime)
    count3 = count3 + 1
else:
    print('The prime numbers are', primelist)






lengthprime = len(primelist)
mean = total/count
format(mean, '.2')
print('The minimum number is', list[0], 'and the maximum is', list[-1], 'and the mean is', mean, 'and the sum is', total)
print('There are', lengthprime, 'prime numbers:', primelist)
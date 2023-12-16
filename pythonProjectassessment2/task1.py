
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






while length != count3:
    prime = list[count3]
    checkPrime(prime)
    count3 = count3 + 1







lengthprime = len(primelist)
mean = total/count
format(mean, '.2')
print('The sum is', total, 'and the minimum number is', list[0], 'and the maximum is', list[-1], 'and the mean is', mean, 'and the sum is', total)
print('There are', lengthprime, 'prime numbers:', primelist)
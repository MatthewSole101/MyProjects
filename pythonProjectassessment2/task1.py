
def checkPrime(x):
    #If the number is greater than 1 and is not divisible by the num - it is prime
    if x > 1:
        for num in range(2, x):
            if x % num == 0:
                return False
        return True
    return False



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
try:
    inp = int(input("Write a integer: "))
    list.append(inp)

    #Repeatedly asking the user for numbers until they say to stop(typing 0)
    while inp != 00:
        inp = int(input("Write another integer or stop by typing '0': "))
        list.append(inp)
        #count is going to be used later to figure out the mean
        count = count + 1

    else:
        #Sorting the list and removing 0 at the end which the user had to put to stop entering numbers
        list.pop(-1)
        length = len(list)
        list.sort()

    while count != count2:
        #Adding up every number and saving it into the variable total
        total = total + list[count2]
        count2 = count2 + 1

    while length != count3:
        #Checks the prime number of every number the user inputted
        if checkPrime(list[count3]):
            primelist.append(list[count3])

        count3 = count3 + 1
#Error Handling
except ValueError:
    print("Wrong value inputted")
    exit()
except TypeError:
    print("Invalid input")
except ZeroDivisionError:
    print("Invalid input")





lengthprime = len(primelist)
#Figuring out the mean of the numbers
mean = total/count
format(mean, '.2')
print('The sum is', total, 'and the minimum number is', list[0], 'and the maximum is', list[-1], 'and the mean is', mean)
print('There are', lengthprime, 'prime numbers:', primelist)

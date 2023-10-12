inp = input('Write a number: ')
count = 0
num = inp[count]
length = len(inp)
answer = 0

numi = int(num)


while count != length:
    answer = numi+answer
    count = count + 1
else:

    print('Your total is', answer)

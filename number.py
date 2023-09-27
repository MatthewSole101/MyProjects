num = int(input("Write a number: "))
#gets last number of a integer
last = int(repr(num)[-1])

if(last == 0 or last == 2 or last == 4 or last == 6 or last == 8 ):
    print("even")
else:
    print("odd")
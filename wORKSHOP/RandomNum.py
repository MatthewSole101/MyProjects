import random


random = random.randint(0, 5)

print(random)

Right = False

while Right != True:
    inp = int(input('Write a number between 0 and 5: '))

    if inp == random:
        print('You guessed right!')
        Right = True
    elif inp != random:
        print('Try again!')
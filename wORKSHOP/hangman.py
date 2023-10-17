import random

list = ['hello', 'crazy', 'nice', 'mad', 'lincoln', 'try', 'happy', 'fame','party', 'pie','cry']

randomnum = random.randint(0,9)

question = list[randomnum]
print(question)

guess = input('What is the word?: ')

while guess != question:
    guess = input('Try again!: ')
else:
    print('You have guessed correct!')

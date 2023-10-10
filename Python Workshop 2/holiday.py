inp = int(input('What is the starting day number?: '))
inp2 = int(input('How long are you staying for?: '))

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

returnday = inp + inp2

if returnday <= 6:
    print('You will return on the', days[returnday])
elif returnday > 6:
    day = returnday % 6
    print('You will return on the', days[day])


    
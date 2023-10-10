inp = int(input('What is the time now?: '))
hm = input('pm or am?')
inph = int(input('How many hours:?; '))
hour = [ 0,13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
min = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


time = inph + inp

num = inp[:1]

if hm == 'pm':
    newtime = hour[time]
    print('The time shold be', newtime,":00", 'when alarm is off')

if hm == 'am':
    if num == 0:
        newtime = min[time]
        print('The time shold be', "0",newtime, ":00", 'when alarm is off')
    else:
        newtime = min[time]
        print('The time shold be', newtime, ":00", 'when alarm is off')


inp = input('Input your password: ')

inp2 = input('Re-enter the password: ')

if inp == inp2:
    print('THe password matches!')
elif inp != inp2:
    print('Password does not match!')
else:
    print('Error')
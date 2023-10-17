ex = False
grades = [[]]



while ex == False:
    inp = input('Write the name of the name of the student or type exit: ')

    if inp == 'exit':
        exit()
    else:
        grades.append(inp)
        print(grades)

    inp2 = int(input('Write the grade: '))
    if inp2 <= 100:
        if inp2 > 50:
            print('You got', inp2, '%')



    grades.append(inp2)
    print(grades)


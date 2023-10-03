inpkilo = float(input("What is your weight in kilos?: "))
inpheight = float(input("What is your height in meters?: "))

bmih = inpheight*inpheight

bmi = inpkilo/bmih

format(bmi, '<fill>><10><,>.<f>')

print('Your bmi is', bmi)
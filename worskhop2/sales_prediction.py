inp = float(input("What are your predicted sales?: "))

counter = 0
conter2 = 0


while counter != 10:
    counter = counter +1
    profitchange = inp/23
    inp = profitchange + inp
    sales = inp/5
    print('Your predicted total profit for year', counter, 'is',inp )
    
else:
    print('end')
def main(l, kg, kl, m, pound, pint):
    inp = int(input('Write in the value: '))
    val = input("What unit is it?(l, kg, kl, m, pound, pint): ")
    
    if inp == 'm':
        print('jellp')
        kl = inp *1.61
        print("It is", kl, "Km")
    elif inp == 'pound':
        kg = inp*0.45
        print("It is", pound, "pounds")
    elif inp == 'pint':
        l = inp*0.57
        print("It is", l, "litres")

    return l, kg, kl, m, pound, pint

main(l=0, kg=0, kl=0, m=0, pound=0, pint=0)
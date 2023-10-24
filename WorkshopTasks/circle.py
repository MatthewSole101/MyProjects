def circ(inpr, inprrr, inpt):
    inp = input("Which shape?(r,t,c): ")

    if inp == 'r':
        inpw = int(input("What is the width?: "))
        inph = int(input("What is the height?: "))

        inpr = inpw * inph
        print("Your rectangle area is", inpr)
    elif inp == 't':
        inpb = int(input("What is the base?: "))
        inph = int(input("What is the height?: "))

        inpt = 0.5 * inpb * inph
        print("The area")
    elif inp == 'c':
        inpy = int(input("What is the radius?: "))
        inprr = inpy * inpy
        inprrr = inprr * 3.14

        print("The area of the circle is", inprr)

    return inpr, inprrr, inpt

circ(inpr=0, inprrr=0, inpt=0)

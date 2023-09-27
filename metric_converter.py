feet = int(input("How many foot are you?"))
inches = int(input("How many inches are you?"))

feet = feet/3.281
inches = inches/39.37

meters = feet+inches

print("You are roughly "+"%f" % meters+" meters tall")
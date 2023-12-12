import math


def solve_quadratic(a,b,c):
    discriminant = (b ** 2) - (4 * a * c)
    sol1 = (-b + math.sqrt(discriminant)) / (2 * a)
    sol2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return sol1, sol2


inp1 = input('Do you want to input a integer or float?(i or f):')

if inp1 == 'i':
    inpa = int(input("Input vaue a"))
    inpb = int(input("Input vaue b"))
    inpc = int(input("Input vaue c"))
    print(solve_quadratic(inpa, inpb, inpc))
elif inp1 == 'f':
    inpa = float(input("Input vaue a"))
    inpb = float(input("Input vaue b"))
    inpc = float(input("Input vaue c"))
    print(solve_quadratic(inpa, inpb, inpc))
else:
    print("Inputed invalid value")
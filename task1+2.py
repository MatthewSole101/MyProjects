import math
class SolveExcep(Exception):
    def __init(self, a):
        print("hello")
        self.a = a
        print(self.a)
        if self.a == 'type error':
            return print("Wrong type inputed")
        elif self.a == 'ZeroDivisionError':
            return print("You can not divide by 0!!")


def solve_quadratic(a,b,c):
    # try:
    #     discriminant = (b**2) - (4*a*c)
    # except TypeError:
    #     SolveExcep('type error')

    try:
        discriminant = (b**2) - (4*a*c)
        sol1 = (-b + math.sqrt(discriminant)) / (2 * a)
        sol2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return sol2, sol2, discriminant

    except ZeroDivisionError:
        SolveExcep('ZeroDivisionError')
    except TypeError:
        SolveExcep('type error')




print(solve_quadratic(5, 5, -6))
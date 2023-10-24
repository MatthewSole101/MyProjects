


def main( answerm, answers, answera):


    num1 = int(input("Write down the first number: "))
    num2 = int(input("Write down the second number: "))

    answerm = num1 * num2
    answers = num1 - num2
    answera = num1 + num2

    print("The multiplication answer is", answerm, "The addition answer is", answera, "The subtraction answer is", answers)


    return answera, answerm, answers


main( answerm=0, answers=0, answera=0)
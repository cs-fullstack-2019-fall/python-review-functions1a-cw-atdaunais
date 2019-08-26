def main():
    printNumbers()
    password = input("Enter a password: ")
    confirm_pass = input("Please confirm your password: ")
    print(checkPassword(password, confirm_pass))
    print(evenOrOdd())
    print(prob4_main(greeting_word()))
    print(quit_func())
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    print(receiveNums(number1, number2))


def printNumbers():
    for index in range(-25, 21, 1):
        print(index)


def checkPassword(orig_pass, confirm):
    if orig_pass == confirm:
        return True
    else:
        return False


def evenOrOdd():
    userInput = int(input("Enter a number. I will say if it's even or odd: "))
    if (userInput % 2) == 0:
        return f"{userInput} is an even number!"
    elif (userInput % 2) == 1:
        return f"{userInput} is an odd number!"


def prob4_main(input):
    return phrase_func(input)


def greeting_word():
    return input("Enter a greeting word: ")


def phrase_func(greeting):
    return f"{greeting} World!"


def quit_func():
    userQuit = ""
    while userQuit != "q":
        userQuit = input("Say anything. Press 'q' to quit: ")
        if userQuit == "q":
            return "Goodbye!"


def receiveNums(num1, num2):
    return f"The sum of {num1} + {num2} is: {num1 + num2}\n" \
           f"The difference of {num1} - {num2} is: {num1 - num2}\n" \
           f"The product of {num1} * {num2} is {num1 * num2}\n" \
           f"The quotient of {num1}/{num2} is: {num1 / num2}"


main()
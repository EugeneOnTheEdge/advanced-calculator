def exponent(num1, num2):
    return int(num1)**int(num2)  #returns num1^num2

def multiply(num1, num2):
    return sum([num1 for i in range(num2)])

def divide(num1, num2):
    answer = int(num1) / int(num2) #returns num1 / num2
    return  int(answer)

if __name__ == "__main__":
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    mode = input("Enter 1 to multiply / 2 to divide / 3 to use num1 exponent num2 / else to exit: ")

    if mode == "1":
        print(str(n1) + " * " + str(n2) + " is " + str(multiply(n1,n2)) + ".")
    elif mode == "2":
        print(str(n1) + " / " + str(n2) + " is " + str(divide(n1,n2)) + ".")
    elif mode == "3":
        print(str(n1) + " ^ " + str(n2) + " is " + str(exponent(n1,n2)) + ".")
    else:
        print("Good bye!")

def add(num1, num2):
    return int(num1) + int(num2)

def divide(num1, num2):
    answer = int(num1) / int(num2)
    return  int(answer)

if __name__ == "__main__":
    n1 = input("Enter the first number: ")
    n2 = input("Enter the second number: ")


print(divide(n1,n2))

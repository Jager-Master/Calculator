#Calculator App

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation from 1/2/3/4: ")
print
print("1. Addition")
print("2. Subtraction")
print("3. Multiply")
print("4. Divide")

while True:

    choice = input("Enter choice (1/2/3/4): ")
    if choice in("1", "2", "3", "4"):
        num1 = float(input("Please enter first number: "))
        num2 = float(input("Please enter second number: "))

        if choice == "1":
            print(num1, "+ ", num2, "= ", add(num1, num2))
        elif choice == "2":
            print(num1, "- ", num2, "= ", subtract(num1, num2))
        elif choice == "3":
            print(num1, "* ", num2, "= ", multiply(num1, num2))
        elif choice == "4":
            print(num1, "/ ", num2, "= ", divide(num1, num2))
        break
    else:
        print("Input invalid")


    

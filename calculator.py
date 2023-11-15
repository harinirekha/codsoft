def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y != 0:
        return x/y
    else:
        return "Error: Division by zero"
def calculator():
    print("Simple Calculator")

    while True:
        try:
            num1 = float(input("Enter the frist number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input.Please enter numberic values.")
            continue
        operation =input("Enter the operation (+,-,*,/): ")
        if operation == '+':
            result = add(num1,num2)
        elif operation == '-':
            result = subtract(num1,num2)
        elif operation == '*':
            result = multiply(num1,num2)
        elif operation == '/':
            print("Invalid operaton,Please enter +,-,*,/.")
            continue 
        print(f"Result: {result}")
        another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != "yes":
            print("Calculator Closed")
            break
calculator()            

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error: Division by zero is undefined."
    return a % b

def Exponentiation(a, b):
    return a ** b 

def calculator():
    print("Simple Calculator")
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return
    
    print("Choose the operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exponentiation (^)")
    
    operation = input("Enter the operation to do: ")
    
    if operation == "1" or operation == "+":
        result = add(num1, num2)
        operation_symbol = "+"
    elif operation == "2" or operation == "-":
        result = subtract(num1, num2)
        operation_symbol = "-"
    elif operation == "3" or operation == "*":
        result = multiply(num1, num2)
        operation_symbol = "*"
    elif operation == "4" or operation == "/":
        result = divide(num1, num2)
        operation_symbol = "/"
    elif operation == "5" or operation == "%":
        result = modulus(num1, num2)
        operation_symbol = "%"   
    elif operation == "4" or operation == "^":
        result = Exponentiation(num1, num2)
        operation_symbol = "^"
    else:
        print("Invalid operation choice.")
        return
    
    print(f"{num1} {operation_symbol} {num2} = {result}")

if __name__ == "__main__":
    calculator()

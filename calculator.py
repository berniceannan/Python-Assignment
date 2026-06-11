print("===== SIMPLE CALCULATOR =====")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, , /, //, %, *): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif operator == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif operator == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

elif operator == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result:.4f}")

elif operator == "//":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 // num2
        print(f"Result: {num1} // {num2} = {result}")

elif operator == "%":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 % num2
        print(f"Result: {num1} % {num2} = {result}")

elif operator == "**":
    result = num1 ** num2
    print(f"Result: {num1} ** {num2} = {result}")

else:
    print(f"Error: '{operator}' is not a valid operator.")

try:
    if result > 0:
        print("The result is positive.")
    elif result < 0:
        print("The result is negative.")
    else:
        print("The result is zero.")
except NameError:
    pass

print("==============================")
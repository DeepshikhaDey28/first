operator = input("Enter any one operator (+ - * /) ")
num1 = float(input("Enter the first number "))
num2 = float(input("Enter the second number "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else :
    print("Symbol not applicable")

print(f"Your total is {result}")
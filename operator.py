def calculator(num1, num2, op):

    if op == '+':
        return num1 + num2

    elif op == '-':
        return num1 - num2

    elif op == '*':
        return num1 * num2

    elif op == '/':
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2

    else:
        return "Invalid operator"


num1 = float(input("First number: "))
num2 = float(input("Second number: "))
op = input("Operator (+, -, *, /): ")

result = calculator(num1, num2, op)
print("Result:", result)

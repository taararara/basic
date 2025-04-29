# Calculate
num1 = int(input("Write first num: "))
num2 = int(input("Write first num: "))
math_operation = input("Press one math. operation: +, -, *, / ")
result = 0
if math_operation == "+":
    result = num1 + num2
elif math_operation == "-":
    result = num1 - num2
elif math_operation == "*":
    result = num1 * num2
elif math_operation == "/":
    if num1 != 0 and num2 != 0:
        result = num1 / num2
    else:
        result = None
        print("cant divide on 0")
if result is not None:
    print(result)

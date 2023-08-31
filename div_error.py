def div(a, b):
    try:
        res = a / b
        return res
    except ZeroDivisionError as e:
        print("ERROR occurred: Division by zero is not allowed")
        return None


numerator = 7
denominator = 0

result = div(numerator, denominator)
if result is not None:
    print("Result: ", result)

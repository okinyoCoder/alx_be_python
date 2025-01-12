def perform_operation (num1, num2, operation):
    x = float(num1)
    y = float(num2)

    match operation:
        case "add":
            return x + y
        case "subtract":
            return x - y
        case "multiply":
            return x * y
        case "divide":
             if num1 == 0 | num2 == 0:
                print("Cannot divide by zero.")
             else:
                return x / y

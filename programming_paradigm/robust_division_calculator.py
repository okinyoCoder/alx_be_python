def safe_divide(numerator, denominator):
    try: 
       x = float(numerator)
       y = float(denominator)
       result = x/y

       print(f"The result of the division is {result}")
    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero.")    
    except ValueError:
        print(f"Error: Please enter numeric values only.")
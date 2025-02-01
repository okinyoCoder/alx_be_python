def safe_divide(numerator, denominator):
    try: 
       x = float(numerator)
       y = float(denominator)
     
       print(f"The result of the division is {x/y}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")    
    except ValueError:
        print("Error: Please enter numeric values only.")
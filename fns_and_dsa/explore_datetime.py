from datetime import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")

def calculate_future_date():
        x = int(input("Enter the number of days to calculate the future date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=x)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future Date after {x} days: {formatted_future_date}")
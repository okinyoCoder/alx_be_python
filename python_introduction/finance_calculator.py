x = int(input("Enter your monthly income: "))
y = int(input("Enter your total monthly expenses: "))

saveM = y - x
print(f"Your monthly savings are ${saveM}")

Projected = saveM * 12 + (saveM * 12 * 0.05)
print("Projected savings after one year, with interest, is: ${Projected}")
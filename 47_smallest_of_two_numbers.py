num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 < num2:
    print("Smallest number =", num1)
elif num2 < num1:
    print("Smallest number =", num2)
else:
    print("Both numbers are equal")

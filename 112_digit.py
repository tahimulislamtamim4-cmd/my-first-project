text = input("Enter a string: ")

digit = 0

for ch in text:
    if ch.isdigit():
        digit += 1

print("Total Digit =", digit)

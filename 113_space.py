text = input("Enter a string: ")

space = 0

for ch in text:
    if ch == " ":
        space += 1

print("Total Space =", space)

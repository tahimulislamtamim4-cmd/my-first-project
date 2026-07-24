text = input("Enter a string: ")

consonant = 0

for ch in text:
    if ch.isalpha() and ch.lower() not in "aeiou":
        consonant += 1

print("Total Consonant =", consonant)

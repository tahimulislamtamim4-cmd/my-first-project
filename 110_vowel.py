text = input("Enter a string: ")

vowel = 0

for ch in text:
    if ch.lower() in "aeiou":
        vowel += 1

print("Total Vowel =", vowel)

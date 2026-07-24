text = input("Enter a string: ")

for ch in sorted(set(text)):
    print(ch, "=", text.count(ch))

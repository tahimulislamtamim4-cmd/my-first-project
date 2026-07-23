text = input("Enter a string: ")

reverse_text = text[::-1]

if text == reverse_text:
    print("Palindrome String")
else:
    print("Not Palindrome String")

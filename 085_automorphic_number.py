n = int(input("Enter a number: "))

square = n * n
temp = n

while temp > 0:
    if temp % 10 != square % 10:
        print("Not Automorphic Number")
        break

    temp = temp // 10
    square = square // 10
else:
    print("Automorphic Number")

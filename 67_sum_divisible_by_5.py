n = int(input("Enter the value of N: "))

sum = 0

for i in range(1, n + 1):
    if i % 5 == 0:
        sum = sum + i

print("Sum =", sum)

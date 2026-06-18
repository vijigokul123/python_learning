print("="*50)
print("      NUMBER STATISTICS")
print("="*50)
n = int(input("How many numbers do you want to enter? "))

sum = 0
largest = None
smallest = None

for i in range(1, n + 1):
    num = int(input("Enter number " + str(i) + ": "))
    sum = sum + num
    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num
average = sum / n

print("\n========== RESULTS ==========")
print("Sum =", sum)
print("Average =", average)
print("Largest Number =", largest)
print("Smallest Number =", smallest)
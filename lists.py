numbers = [10, 45, 23, 89, 12]
rev_list = numbers[::-1]

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print("Original list:", numbers)
print("Reversed list:", rev_list)
print("Largest element:", largest)
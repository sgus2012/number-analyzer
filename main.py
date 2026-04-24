numbers = [3, 7, 2, 9, 4, 6, 1]

total = 0
max_num = numbers[0]
count_even = 0

i = 0

while i < len(numbers):
    total += numbers[i]

    if numbers[i] > max_num:
        max_num = numbers[i]

    if numbers[i] % 2 == 0:
        count_even += 1

    i += 1

print("Sum:", total)
print("Max:", max_num)
print("Even count:", count_even)

numbers = [0, 1, 0, 3, 0, 12]

result = []
zero_count = 0

for num in numbers:
    if num == 0:
        zero_count += 1
    else:
        result.append(num)

result.extend([0] * zero_count)

print("After moving zeroes to the end:", result)
distance = float(input())

if distance <= 2:
    fare = 50
else:
    fare = 50 + (distance - 2) * 10

print(int(fare))
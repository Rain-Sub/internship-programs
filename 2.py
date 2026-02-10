numbers=[10,43,1,43,10,1]
unique=[]
for num in numbers:
    if num not in unique:
        unique.append(num)
print("list after removing duplicate from numbers",unique)


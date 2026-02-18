try:
    # Step 1: Create numbers.txt and store 1-20
    with open("numbers.txt", "w") as file:
        for i in range(1, 21):
            file.write(str(i) + "\n")
    print("✅ 'numbers.txt' created with numbers 1 to 20.\n")

    # Step 2: Read numbers from the file
    even_numbers = []
    odd_numbers = []

    with open("numbers.txt", "r") as file:
        for line in file:
            num = int(line.strip())  # Convert string to int
            if num % 2 == 0:
                even_numbers.append(num)
            else:
                odd_numbers.append(num)

    # Step 3: Print even and odd numbers
    print("Even Numbers:", even_numbers)
    print("Odd Numbers:", odd_numbers)

except Exception as e:
    print("❌ Error:", e)

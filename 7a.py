# Create and write numbers 1 to 20 into numbers.txt

try:
    with open("numbers.txt", "w") as file:
        for i in range(1, 21):
            file.write(str(i) + "\n")

    print("✅ File 'numbers.txt' created successfully with numbers 1 to 20.")

except Exception as e:
    print("❌ Error occurred:", e)

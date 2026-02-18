from collections import Counter
import re

file_name = "words_file.txt"

# Step 1: Create a file and write some words
try:
    with open(file_name, "w") as f:
        f.write("apple banana apple orange banana apple grape mango orange mango banana apple")
    print(f"File '{file_name}' created and words written.\n")
except IOError as e:
    print(f"Error creating file: {e}")

# Step 2: Read the file and process words
try:
    with open(file_name, "r") as f:
        content = f.read()
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except IOError as e:
    print(f"Error reading file: {e}")
else:
    # Normalize text: lowercase and split into words
    words = re.findall(r'\b\w+\b', content.lower())

    # Count word occurrences
    word_counts = Counter(words)

    # Step 3: Print analysis of all words
    print("Word analysis in file:")
    for word, count in word_counts.items():
        if count > 1:
            print(f"'{word}' exists and repeats {count} times")
        else:
            print(f"'{word}' exists and occurs once")

    # Step 4: Allow user to check other words
    while True:
        user_word = input("\nEnter a word to check its occurrence (or type 'exit' to stop): ").strip().lower()
        if user_word == "exit":
            print("Exiting word check.")
            break
        elif user_word in word_counts:
            count = word_counts[user_word]
            if count > 1:
                print(f"'{user_word}' exists and repeats {count} times")
            else:
                print(f"'{user_word}' exists and occurs once")
        else:
            print(f"'{user_word}' does not exist in the file")

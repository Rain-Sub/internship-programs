# Program to sort sentence based on numbers inside words

sentence = input("Enter the sentence: ")
words = sentence.split()

result = [""] * len(words)

for word in words:
    for ch in word:
        if ch.isdigit():
            position = int(ch)
            clean_word = word.replace(ch, "")
            result[position] = clean_word

print("Output:", " ".join(result))
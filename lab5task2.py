sentence = input("Enter a sentence: ")

print("Number of characters:", len(sentence))
print("Number of words:", len(sentence.split()))

vowels = 0
spaces = 0
digits = 0

for char in sentence:
    if char.lower() in "aeiou":
        vowels += 1
    elif char == " ":
        spaces += 1
    elif char.isdigit():
        digits += 1

print("Number of vowels:", vowels)
print("Number of spaces:", spaces)
print("Number of digits:", digits)
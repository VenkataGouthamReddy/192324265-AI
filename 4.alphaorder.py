# Input sentence
sentence = "Sorting a sentence in alphabetical order"

# Split the sentence into words
words = sentence.split()

# Sort the words in alphabetical order
for i in range(len(words)):
    for j in range(i + 1, len(words)):
        if words[i].lower() > words[j].lower():
            words[i], words[j] = words[j], words[i]

# Join the sorted words back into a sentence
sorted_sentence = ' '.join(words)

# Print the sorted sentence
print(sorted_sentence)

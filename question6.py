# Open the file in read mode
with open("test.txt", "r") as file:
    # Create an empty dictionary to store word occurrences
    word_count = {}

    # Read each line from the file
    for line in file:
        # Remove leading spaces and newline characters
        line = line.strip()

        # Convert the line to lowercase to avoid case mismatch
        line = line.lower()

        # Split the line into words
        words = line.split()

        # Iterate over each word in the line
        for word in words:
            # Update the word count in the dictionary
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

# Print the occurrences of each word
for word, count in word_count.items():
    print(f"{word}: {count}")

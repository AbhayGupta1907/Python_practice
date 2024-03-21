def count_statistics(line):
    lower_count = upper_count = digit_count = alpha_count = 0

    for char in line:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
        elif char.isdigit():
            digit_count += 1
        if char.isalpha():
            alpha_count += 1

    print(f"Number of uppercase letters: {upper_count}")
    print(f"Number of lowercase letters: {lower_count}")
    print(f"Number of alphabets: {alpha_count}")
    print(f"Number of digits: {digit_count}")

# Input from the user
user_input = input("Enter a string/line/sentence: ")
count_statistics(user_input)

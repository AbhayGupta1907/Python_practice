def count_vowels_iterative(s):
    vowels = "AEIOUaeiou"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

user_input = input("Enter a string: ")
num_vowels = count_vowels_iterative(user_input)
print(f"Number of vowels in the string: {num_vowels}")

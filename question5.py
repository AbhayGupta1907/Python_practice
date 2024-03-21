def remove_vowels_replace(s):
    vowels = "AEIOUaeiou"
    for vowel in vowels:
        s = s.replace(vowel, "")
    return s

user_input = input("Enter a string: ")
result = remove_vowels_replace(user_input)
print(f"The string after removing vowels: {result}")

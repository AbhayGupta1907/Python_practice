def reverse_incremental_string(s):
    return ''.join([s[i] for i in range(len(s) - 1, -1, -1)])

original_string = "GeeksforGeeks"
reversed_string = reverse_incremental_string(original_string)
print(f"The original string is: {original_string}")
print(f"The reversed string is: {reversed_string}")

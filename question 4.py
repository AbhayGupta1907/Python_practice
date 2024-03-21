def are_distinct(s, i, j):
    visited = [False] * 256
    for k in range(i, j + 1):
        if visited[ord(s[k])]:
            return False
        visited[ord(s[k])] = True
    return True

def longest_unique_substring(s):
    n = len(s)
    result = 0
    for i in range(n):
        for j in range(i, n):
            if are_distinct(s, i, j):
                result = max(result, j - i + 1)
    return result

# Input from the user
user_input = input("Enter a string: ")
length = longest_unique_substring(user_input)
print(f"The length of the longest non-repeating character substring is {length}")

def compute_prefix_function(pattern):
    m = len(pattern)
    prefix_function = [0] * m
    j = 0

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix_function[j - 1]

        if pattern[i] == pattern[j]:
            j += 1

        prefix_function[i] = j

    return prefix_function


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    prefix_function = compute_prefix_function(pattern)
    j = 0

    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = prefix_function[j - 1]

        if text[i] == pattern[j]:
            j += 1

        if j == m:
            print("Pattern found at index", i - m + 1)
            j = prefix_function[j - 1]

# Example usage:
text = "ababcababcabcabc"
pattern = "abcabc"
kmp_search(text, pattern)

def find_first_occurence_of_substring(haystack: str, needle: str) -> int:
    i = -1
    n = len(haystack)

    for idx in range(n - len(needle) + 1):
        if haystack[idx:idx + len(needle)] == needle:
            i = idx
            break
    return i

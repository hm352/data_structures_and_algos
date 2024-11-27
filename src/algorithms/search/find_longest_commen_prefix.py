# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".


def longest_prefix(strings: [str]) -> str:
    longest = ''
    shortest_word = min(strings, key=len)
    for i, char in enumerate(shortest_word):
        prefix = [c for c in strings if c[i] == char]
        if len(prefix) == len(strings):
            longest += char
        else:
            break
    return longest

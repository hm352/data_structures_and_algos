# This is originally from the leet code question
# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1464159977/?envType=problem-list-v2&envId=string&
# Diffculty: Medium
# Below I have attempted several different solutions

def longest_substring_set_sliding_window(s: str) -> int:
    # This uses a sliding window pattern to
    # find the longest non repeating substring
    # The set is used to keep track of the unique characters
    # When a character is repeated, the start index is incremented
    max_length = 0
    sub = set()
    start = 0
    for i in range(len(s)):
        while s[i] in sub:
            sub.remove(s[start])
            start += 1
        sub.add(s[i])
        max_length = max(max_length, i - start + 1)
    return max_length

# def longest_substring_hashtable(s: str) -> int:
#     # The hashmap stores the most recent index of each character
#     # by checking if a character has been seen before
#     # If it has, the start index is incremented
#     # If it hasn't, the character is added to the hashtable
#     #
#     max_length = 0
#     start = 0
#     char_index = {}
#     for i in range(len(s)):
#         v = s[i]
#         if v not in char_index or char_index[v] < start:
#             char_index[v] = i
#             max_length = max(max_length, char_index[v] - char_index[s[start]] + 1)
#         else:
#             start += 1
#             char_index[v] = i
#     return max_length

def longest_substring_hashtable(s: str) -> int:
    # The hashmap stores the most recent index of each character
    # by checking if a character has been seen before
    # If it has, the start index is incremented
    # If it hasn't, the character is added to the hashtable
    #
    max_length = 0
    start = 0
    char_index = {}
    for i in range(len(s)):
        v = s[i]
        if v in char_index and char_index[v] >= start:
            start = char_index[v] + 1
        char_index[v] = i
        max_length = max(max_length, char_index[v] - char_index[s[start]] + 1)
    return max_length

if __name__ == "__main__":
    print(longest_substring_set_sliding_window("abcabcbb"))
    print(longest_substring_set_sliding_window("bbbbb"))
    print(longest_substring_set_sliding_window("pwwkew"))
    print(longest_substring_set_sliding_window(""))
    print(longest_substring_set_sliding_window("dvdf"))
    print(longest_substring_set_sliding_window(" "))
    print('-----------------')
    print(longest_substring_hashtable("abcabcbb"))
    print(longest_substring_hashtable("bbbbb"))
    print(longest_substring_hashtable("pwwkew"))
    print(longest_substring_hashtable(""))
    print(longest_substring_hashtable("dvdf"))
    print(longest_substring_hashtable(" "))

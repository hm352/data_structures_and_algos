from collections import Counter
def longest_anagram(a: str , b: str) -> int:
    counter_a = Counter(a)
    counter_b = Counter(b)
    diff_a = counter_a - counter_b
    diff_b = counter_b - counter_a
    return sum(diff_a.values()) + sum(diff_b.values())


if __name__ == '__main__':
    a = 'fcrxzwscanmligyxyvym'
    b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'
    print(longest_anagram(a, b))

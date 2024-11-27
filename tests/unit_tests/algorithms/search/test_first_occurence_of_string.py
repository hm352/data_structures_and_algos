from src.algorithms.search.first_index_of_substring import find_first_occurence_of_substring
import pytest

@pytest.mark.parametrize("haystack, needle, expected", [
    ("sadbutsad", "sad", 0),
    ("leetcode", "leeto", -1),
]
)

def test_first_occurence_of_substring(haystack, needle, expected):
    actual = find_first_occurence_of_substring(haystack, needle)
    assert actual == expected

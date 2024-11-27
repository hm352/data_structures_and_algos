from src.algorithms.search.find_longest_commen_prefix import longest_prefix
import pytest

@pytest.mark.parametrize("strings, expected", [
    (["flower", "flow", "flight"], "fl"),
    (["dog", "racecar", "car"], ""),
])

def test_longest_common_prefix(strings, expected):
    actual = longest_prefix(strings)
    assert actual == expected

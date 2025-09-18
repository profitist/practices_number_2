import pytest
from prefix_search import *


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (['python', 'yhon', 'kontur', 'ontur'], (5, ('kontur', 'ontur'))),
        (['tochka', 'www', 'def', 'f', 'example.com'], (1, ('def', 'f'))),
        (['arbuz', 'airbus', 'buzz', 'stop'], (3, ('arbuz', 'buzz'))),
        (['python', 'python', 'friend', 'ending'], (3, ('friend', 'ending'))),
        (['hello', 'world'], (0, None)),
        (['a', 'aa', 'aaa'], (2, ('aa', 'aaa'))),
        (['abc', 'bcd', 'cde'], (2, ('abc', 'bcd'))),
        (['same', 'same'], (0, None)),
        ([], (0, None)),
        (['word'], (0, None)),
    ]
)
def test_brute_solution(test_input, expected):
    assert bruteforce(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (['python', 'yhon', 'kontur', 'ontur'], (5, ('kontur', 'ontur'))),
        (['tochka', 'www', 'def', 'f', 'example.com'], (1, ('def', 'f'))),
        (['arbuz', 'airbus', 'buzz', 'stop'], (3, ('arbuz', 'buzz'))),
        (['python', 'python', 'friend', 'ending'], (3, ('friend', 'ending'))),
        (['hello', 'world'], (0, None)),
        (['a', 'aa', 'aaa'], (2, ('aa', 'aaa'))),
        (['abc', 'bcd', 'cde'], (2, ('abc', 'bcd'))),
        (['same', 'same'], (0, None)),
        ([], (0, None)),
        (['word'], (0, None)),
    ]
)
def test_dict_solution(test_input, expected):
    assert dict_find(test_input) == expected


if __name__ == '__main__':
    pytest.main()

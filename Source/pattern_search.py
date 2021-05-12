"""

O(mn)
"""


def search(text, pattern):
    _results = []

    for i in range(len(text) - len(pattern)):
        found = True

        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                found = False
                break

        if found:
            _results.append(i)

    return _results

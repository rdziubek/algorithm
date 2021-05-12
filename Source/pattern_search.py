"""

O(mn)
"""


def search(text, pattern):
    results = []

    for i in range(len(text) - len(pattern)):
        found = True

        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                found = False
                break

        if found:
            results.append(i)

    return results

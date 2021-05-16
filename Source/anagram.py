"""

O(m + n)
"""


def anagram(word1, word2):
    counts = [0] * 128
    for i in range(len(word1)):
        counts[ord(word1[i])] += 1
    for i in range(len(word2)):
        counts[ord(word2[i])] -= 1

    for i in range(128):
        if counts[i] != 0:
            return False

    return True

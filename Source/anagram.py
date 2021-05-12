"""

O(m + n)
"""


def anagram(word, word2):
    if len(word) != len(word2):
        return False

    counts = [0] * 128
    for i in range(len(word)):
        counts[ord(word[i])] += 1
    for i in range(len(word2)):
        counts[ord(word2[i])] -= 1

    for i in range(128):
        if counts[i] != 0:
            return False

    return True


print(anagram(list('arbuz'), list('burza')))

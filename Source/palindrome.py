"""

O(n)
"""


def palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - 1 - i]:
            return False

    return True


print(palindrome(list('kajak')))

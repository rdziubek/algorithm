"""

O(mn)
"""


def cipher_custom(key, alphabet, text):
    result = []

    for i in range(len(text)):
        for j in range(len(alphabet)):
            if text[i] == alphabet[j]:
                result += [alphabet[(j + key) % len(alphabet)]]

    return result


print(cipher_custom(2, list('abcdefghijklmnopqrstuvwxyz'), list('xyz')))

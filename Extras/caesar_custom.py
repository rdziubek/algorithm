"""

O(mn)
"""


def cipher(key, alphabet, text):
    result = []

    for i in range(len(text)):
        for j in range(len(alphabet)):
            if text[i] == alphabet[j]:
                result += [alphabet[(j + key) % len(alphabet)]]

    return result


"""EVALUATION"""
cipher(
    key=2,
    alphabet=list('abcdefghijklmnopqrstuvwxyz'),
    text=list('xyz')
)

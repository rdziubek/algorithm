"""

O(n)
"""


def cipher(key: int, text):
    result = []

    for i in range(len(text)):
        candidate: int = ord(text[i]) + key

        if candidate > ord('z'):
            candidate -= 26
        elif candidate < ord('a'):
            candidate += 26

        result.append(chr(candidate))

    return result


print(cipher(2, 'xyz'))

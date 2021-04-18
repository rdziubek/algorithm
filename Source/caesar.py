"""

O(n)
"""


def cipher(key, text):
    result = []

    for i in range(len(text)):
        candidate = ord(text[i]) + key

        if candidate > ord('z'):
            candidate -= 26
        elif candidate < ord('a'):
            candidate += 26

        result += [chr(candidate)]

    return result


print(cipher(2, 'xyz'))

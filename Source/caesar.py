"""

O(n)
"""


def cipher(key, text):
    for i in range(len(text)):
        candidate = ord(text[i]) + key

        if candidate > ord('z'):
            candidate -= 26
        elif candidate < ord('a'):
            candidate += 26

        text[i] = chr(candidate)

    return text


print(cipher(2, list('xyz')))

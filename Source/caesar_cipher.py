"""
1. Replace each character:
    (character + key) mod 26

NOTE:
    For the formula to be applied, ASCII needs to be zeroed out by subtracting the value
    of either 'a' or 'A' (1), depending on the case (2). (and later adding the value back)

    (1)
        (character + key - 'a'|'A') mod 26 + 'a'|'A'

    (2)
        'a' <= character <= 'z': 'a'
        'A' <= character <= 'Z': 'A'

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

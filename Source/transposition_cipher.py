"""
    SLOWO   ->  LSWOO

    Letters adjacent to each other are swapped;
    if no adjacent found, left as is.

O(n)
"""


def cipher(text):
    for i in range(1, len(text), 2):
        preceding = text[i - 1]
        text[i - 1] = text[i]
        text[i] = preceding

    return text
